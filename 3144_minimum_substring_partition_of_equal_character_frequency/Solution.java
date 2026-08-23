// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    private String s;
    private int n;
    private int[] memo;

    private int dfs(int i) {
        if (i >= n) return 0;
        if (memo[i] != -1) return memo[i];
        int[] cnt = new int[26];
        Map<Integer, Integer> freq = new HashMap<>();
        memo[i] = n - i;
        for (int j = i; j < n; j++) {
            int k = s.charAt(j) - 'a';
            if (cnt[k] > 0) {
                int c = cnt[k];
                int nv = freq.get(c) - 1;
                if (nv == 0) freq.remove(c);
                else freq.put(c, nv);
            }
            cnt[k]++;
            freq.put(cnt[k], freq.getOrDefault(cnt[k], 0) + 1);
            if (freq.size() == 1) {
                memo[i] = Math.min(memo[i], 1 + dfs(j + 1));
            }
        }
        return memo[i];
    }

    public int minimumSubstringsInPartition(String s) {
        this.s = s;
        this.n = s.length();
        this.memo = new int[n];
        Arrays.fill(memo, -1);
        return dfs(0);
    }
}
