// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

using System.Text;

public class Solution {
    public string LexPalindromicPermutation(string s, string target) {
        int[] cnt = new int[26];
        foreach (char ch in s) cnt[ch - 'a']++;
        int odd = 0, mid = -1;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2 == 1) { odd++; mid = i; }
        }
        if (odd > 1) return "";
        int[] half = new int[26];
        for (int i = 0; i < 26; i++) half[i] = cnt[i] / 2;
        int n = s.Length;
        int halfLen = n / 2;
        char[] left = new char[halfLen];
        bool Dfs(int pos, bool greater) {
            if (pos == halfLen) {
                if (mid >= 0) {
                    if (greater) return true;
                    return (char)('a' + mid) > target[halfLen];
                }
                return greater;
            }
            int start = greater ? 0 : (target[pos] - 'a');
            for (int c = start; c < 26; c++) {
                if (half[c] == 0) continue;
                half[c]--;
                left[pos] = (char)('a' + c);
                if (Dfs(pos + 1, greater || c > (target[pos] - 'a'))) return true;
                half[c]++;
            }
            return false;
        }
        if (!Dfs(0, false)) return "";
        var sb = new StringBuilder();
        sb.Append(left);
        if (mid >= 0) sb.Append((char)('a' + mid));
        for (int i = halfLen - 1; i >= 0; i--) sb.Append(left[i]);
        string res = sb.ToString();
        if (string.CompareOrdinal(res, target) <= 0) return "";
        return res;
    }
}
