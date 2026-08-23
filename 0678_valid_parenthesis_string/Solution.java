// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

class Solution {
    public boolean checkValidString(String s) {
        int lo = 0;
        int hi = 0;
        for (int i = 0; i < s.length(); ++i) {
            char ch = s.charAt(i);
            if (ch == '(') {
                ++lo;
                ++hi;
            } else if (ch == ')') {
                lo = Math.max(lo - 1, 0);
                --hi;
                if (hi < 0) {
                    return false;
                }
            } else {
                lo = Math.max(lo - 1, 0);
                ++hi;
            }
        }
        return lo == 0;
    }
}
