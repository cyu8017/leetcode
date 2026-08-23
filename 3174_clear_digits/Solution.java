// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

class Solution {
    public String clearDigits(String s) {
        StringBuilder stk = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                stk.deleteCharAt(stk.length() - 1);
            } else {
                stk.append(c);
            }
        }
        return stk.toString();
    }
}
