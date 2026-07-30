// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

using System.Collections.Generic;
public class Solution {
    const int MOD = 1000000007;
    int[][] trans; int n, m; string s1, s2, evil;
    Dictionary<(int,int,bool,bool), int> memo = new Dictionary<(int,int,bool,bool), int>();
    public int FindGoodStrings(int n, string s1, string s2, string evil) {
        this.n = n; this.s1 = s1; this.s2 = s2; this.evil = evil; m = evil.Length;
        var pi = new int[m];
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            while (j > 0 && evil[i] != evil[j]) j = pi[j - 1];
            if (evil[i] == evil[j]) j++;
            pi[i] = j;
        }
        trans = new int[m][];
        for (int j = 0; j < m; j++) {
            trans[j] = new int[26];
            for (int x = 0; x < 26; x++) {
                char c = (char)('a' + x); int k = j;
                while (k > 0 && evil[k] != c) k = pi[k - 1];
                if (evil[k] == c) k++;
                trans[j][x] = k;
            }
        }
        return Dp(0, 0, true, true);
    }
    int Dp(int i, int j, bool lo, bool hi) {
        if (j == m) return 0;
        if (i == n) return 1;
        var key = (i, j, lo, hi);
        if (memo.ContainsKey(key)) return memo[key];
        int a = lo ? s1[i] - 'a' : 0, b = hi ? s2[i] - 'a' : 25, ans = 0;
        for (int x = a; x <= b; x++)
            ans = (ans + Dp(i + 1, trans[j][x], lo && x == a, hi && x == b)) % MOD;
        return memo[key] = ans;
    }
}
