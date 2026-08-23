// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

class Solution {
    boolean isContiguous(char a, char b) {
        int x = Math.abs(a - b);
        return x == 1 || x == 25;
    }
    public String resultingString(String s) {
        StringBuilder stk = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (stk.length() > 0 && isContiguous(stk.charAt(stk.length() - 1), c))
                stk.deleteCharAt(stk.length() - 1);
            else stk.append(c);
        }
        return stk.toString();
    }
}
