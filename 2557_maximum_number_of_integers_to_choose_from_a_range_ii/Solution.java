// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private int ans;
    private long remain;

    public int maxCount(int[] banned, int n, long maxSum) {
        Arrays.sort(banned);
        List<Integer> uniq = new ArrayList<>();
        for (int x : banned) {
            if (x >= 1 && x <= n && (uniq.isEmpty() || uniq.get(uniq.size() - 1) != x)) uniq.add(x);
        }
        ans = 0;
        remain = maxSum;
        int prev = 0;
        for (int b : uniq) {
            check(prev + 1L, b - 1L);
            prev = b;
        }
        check(prev + 1L, n);
        return ans;
    }

    private void check(long l, long r) {
        if (l > r || remain <= 0) return;
        long lo = l, hi = r, best = l - 1;
        while (lo <= hi) {
            long mid = (lo + hi) / 2;
            long cnt = mid - l + 1;
            long sum = (l + mid) * cnt / 2;
            if (sum <= remain) {
                best = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        if (best >= l) {
            int cnt = (int) (best - l + 1);
            ans += cnt;
            remain -= (l + best) * cnt / 2;
        }
    }
}
