// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

using System.Collections.Generic;

public class Solution {
    public int PossibleStringCount(string word, int k) {
        const int mod = 1000000007;
        var groups = new List<int>();
        for (int i = 0; i < word.Length; ) {
            int j = i;
            while (j < word.Length && word[j] == word[i]) j++;
            groups.Add(j - i);
            i = j;
        }
        int total = 1;
        foreach (int g in groups) total = (int)((long)total * g % mod);
        if (k <= groups.Count) return total;
        int need = k - 1;
        int[] dp = new int[need];
        dp[0] = 1;
        foreach (int g in groups) {
            int[] ndp = new int[need];
            int[] pref = new int[need + 1];
            for (int i = 0; i < need; i++) pref[i + 1] = (pref[i] + dp[i]) % mod;
            for (int s = 0; s < need; s++) {
                int lo = s - g;
                if (lo < 0) lo = 0;
                int hi = s - 1;
                if (hi >= 0) ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod;
            }
            dp = ndp;
        }
        int bad = 0;
        foreach (int v in dp) bad = (bad + v) % mod;
        return (total - bad + mod) % mod;
    }
}
