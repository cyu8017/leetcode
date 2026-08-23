// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

class Solution {
    public String smallestPalindrome(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        StringBuilder t = new StringBuilder();
        char ch = 0;
        for (char c = 'a'; c <= 'z'; c++) {
            int v = cnt[c - 'a'] / 2;
            for (int i = 0; i < v; i++) t.append(c);
            cnt[c - 'a'] -= v * 2;
            if (cnt[c - 'a'] == 1) ch = c;
        }
        StringBuilder sb = new StringBuilder(t);
        if (ch != 0) sb.append(ch);
        for (int i = t.length() - 1; i >= 0; i--) sb.append(t.charAt(i));
        return sb.toString();
    }
}
