// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumSubstringsInPartition(string s) {
        int n = s.Length;
        int[] memo = new int[n];
        for (int i = 0; i < n; i++) memo[i] = -1;
        int Dfs(int i) {
            if (i >= n) return 0;
            if (memo[i] != -1) return memo[i];
            int[] cnt = new int[26];
            var freq = new Dictionary<int, int>();
            memo[i] = n - i;
            for (int j = i; j < n; j++) {
                int k = s[j] - 'a';
                if (cnt[k] > 0) {
                    if (--freq[cnt[k]] == 0) freq.Remove(cnt[k]);
                }
                cnt[k]++;
                if (!freq.ContainsKey(cnt[k])) freq[cnt[k]] = 0;
                freq[cnt[k]]++;
                if (freq.Count == 1) {
                    memo[i] = Math.Min(memo[i], 1 + Dfs(j + 1));
                }
            }
            return memo[i];
        }
        return Dfs(0);
    }
}
