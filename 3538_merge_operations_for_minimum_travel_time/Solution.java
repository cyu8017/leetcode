// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

import java.util.HashMap;
import java.util.Map;

class Solution {
    int n, k;
    int[] position, prefix;
    Map<String, Long> memo;
    static final long INF = (long) 1e18;

    public int minTravelTime(int l, int n, int k, int[] position, int[] time) {
        this.n = n;
        this.k = k;
        this.position = position;
        prefix = new int[n];
        prefix[0] = time[0];
        for (int i = 1; i < n; i++) prefix[i] = prefix[i - 1] + time[i];
        memo = new HashMap<>();
        return (int) dp(0, k, 0);
    }

    long dp(int i, int skips, int last) {
        if (i == n - 1) return skips == 0 ? 0 : INF;
        String key = i + "," + skips + "," + last;
        if (memo.containsKey(key)) return memo.get(key);
        int rate = prefix[i];
        if (last > 0) rate -= prefix[last - 1];
        long res = INF;
        int end = n - 1;
        if (i + skips + 1 < end) end = i + skips + 1;
        for (int j = i + 1; j <= end; j++) {
            long cand = 1L * (position[j] - position[i]) * rate + dp(j, skips - (j - i - 1), i + 1);
            if (cand < res) res = cand;
        }
        memo.put(key, res);
        return res;
    }
}
