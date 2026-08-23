// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution {
    public String firstPalindrome(String[] words) {
        for (String w : words) {
            boolean ok = true;
            for (int l = 0, r = w.length() - 1; l < r; l++, r--)
                if (w.charAt(l) != w.charAt(r)) { ok = false; break; }
            if (ok) return w;
        }
        return "";
    }
}
