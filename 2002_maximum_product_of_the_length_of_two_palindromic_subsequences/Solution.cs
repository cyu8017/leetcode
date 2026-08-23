// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

using System.Text;

public class Solution {
    public int MaxProduct(string s) {
        int n = s.Length;
        (bool ok, int len) IsPal(int mask) {
            var chars = new StringBuilder();
            for (int i = 0; i < n; i++) if ((mask & (1 << i)) != 0) chars.Append(s[i]);
            for (int l = 0, r = chars.Length - 1; l < r; l++, r--)
                if (chars[l] != chars[r]) return (false, 0);
            return (true, chars.Length);
        }
        int best = 0, total = 1 << n;
        for (int mask1 = 1; mask1 < total; mask1++) {
            var (ok1, len1) = IsPal(mask1);
            if (!ok1) continue;
            int remain = (total - 1) ^ mask1;
            for (int mask2 = remain; mask2 > 0; mask2 = (mask2 - 1) & remain) {
                var (ok2, len2) = IsPal(mask2);
                if (ok2 && len1 * len2 > best) best = len1 * len2;
            }
        }
        return best;
    }
}
