// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

using System.Collections.Generic;

public class Solution {
    public bool PossiblyEquals(string s1, string s2) {
        int n = s1.Length, m = s2.Length;
        var memo = new Dictionary<(int, int, int), bool>();
        bool IsDigit(char c) => c >= '0' && c <= '9';
        bool Dfs(int i, int j, int diff) {
            var key = (i, j, diff);
            if (memo.TryGetValue(key, out bool cached)) return cached;
            if (i == n && j == m) return memo[key] = (diff == 0);
            bool res = false;
            if (diff == 0 && i < n && j < m && !IsDigit(s1[i]) && !IsDigit(s2[j])) {
                if (s1[i] == s2[j]) res = Dfs(i + 1, j + 1, 0);
            } else if (diff > 0 && i < n && !IsDigit(s1[i])) {
                res = Dfs(i + 1, j, diff - 1);
            } else if (diff < 0 && j < m && !IsDigit(s2[j])) {
                res = Dfs(i, j + 1, diff + 1);
            }
            if (!res && i < n && IsDigit(s1[i])) {
                int val = 0;
                for (int p = i; p < n && IsDigit(s1[p]); p++) {
                    val = val * 10 + (s1[p] - '0');
                    if (Dfs(p + 1, j, diff + val)) { res = true; break; }
                }
            }
            if (!res && j < m && IsDigit(s2[j])) {
                int val = 0;
                for (int p = j; p < m && IsDigit(s2[p]); p++) {
                    val = val * 10 + (s2[p] - '0');
                    if (Dfs(i, p + 1, diff - val)) { res = true; break; }
                }
            }
            return memo[key] = res;
        }
        return Dfs(0, 0, 0);
    }
}
