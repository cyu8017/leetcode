// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution {
    public boolean canBeValid(String s, String locked) {
        int n = s.length();
        if (n % 2 != 0) return false;
        int bal = 0;
        for (int i = 0; i < n; i++) {
            if (locked.charAt(i) == '0' || s.charAt(i) == '(') bal++;
            else bal--;
            if (bal < 0) return false;
        }
        bal = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (locked.charAt(i) == '0' || s.charAt(i) == ')') bal++;
            else bal--;
            if (bal < 0) return false;
        }
        return true;
    }
}
