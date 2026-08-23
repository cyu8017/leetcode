// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

class Solution {
    public String decodeAtIndex(String s, int k) {
        long size = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) size *= ch - '0';
            else size++;
        }
        long kk = k;
        for (int i = s.length() - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            kk %= size;
            if (kk == 0 && Character.isLetter(ch)) return String.valueOf(ch);
            if (Character.isDigit(ch)) size /= ch - '0';
            else size--;
        }
        return "";
    }
}
