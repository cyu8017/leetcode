// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

using System.Collections.Generic;

public class Solution {
    static int BitsPop(int x) {
        int c = 0;
        while (x > 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }

    public int CountKReducibleNumbers(string s, int k) {
        const int mod = 1000000007;
        int[] red = new int[801];
        red[1] = 0;
        for (int i = 2; i <= 800; i++) red[i] = 1 + red[BitsPop(i)];
        int n = s.Length;
        var memo = new Dictionary<(int, int, int), int>();
        int Dfs(int pos, bool tight, int ones) {
            if (pos == n) {
                if (ones == 0) return 0;
                return red[ones] <= k - 1 ? 1 : 0;
            }
            var key = (pos, tight ? 1 : 0, ones);
            if (memo.ContainsKey(key)) return memo[key];
            int up = tight ? (s[pos] - '0') : 1;
            int ans = 0;
            for (int d = 0; d <= up; d++) {
                bool nt = tight && d == up;
                ans = (ans + Dfs(pos + 1, nt, ones + d)) % mod;
            }
            return memo[key] = ans;
        }
        return Dfs(0, true, 0);
    }
}
