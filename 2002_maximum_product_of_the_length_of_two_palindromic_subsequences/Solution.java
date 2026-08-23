// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution {
    public int maxProduct(String s) {
        int n = s.length();
        int best = 0, total = 1 << n;
        for (int mask1 = 1; mask1 < total; mask1++) {
            int len1 = palLen(s, mask1);
            if (len1 == 0) continue;
            int remain = (total - 1) ^ mask1;
            for (int mask2 = remain; mask2 > 0; mask2 = (mask2 - 1) & remain) {
                int len2 = palLen(s, mask2);
                if (len2 > 0 && len1 * len2 > best) best = len1 * len2;
            }
        }
        return best;
    }

    private int palLen(String s, int mask) {
        StringBuilder chars = new StringBuilder();
        for (int i = 0; i < s.length(); i++)
            if ((mask & (1 << i)) != 0) chars.append(s.charAt(i));
        for (int l = 0, r = chars.length() - 1; l < r; l++, r--)
            if (chars.charAt(l) != chars.charAt(r)) return 0;
        return chars.length();
    }
}
