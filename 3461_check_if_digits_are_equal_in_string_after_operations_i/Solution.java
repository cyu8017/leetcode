// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution {
    public boolean hasSameDigits(String s) {
        char[] b = s.toCharArray();
        while (b.length > 2) {
            char[] nb = new char[b.length - 1];
            for (int i = 0; i + 1 < b.length; i++) {
                nb[i] = (char) ('0' + (b[i] - '0' + b[i + 1] - '0') % 10);
            }
            b = nb;
        }
        return b[0] == b[1];
    }
}
