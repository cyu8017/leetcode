// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

class Solution {
    public String makeGood(String s) {
        StringBuilder stack = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (stack.length() > 0) {
                char top = stack.charAt(stack.length() - 1);
                if (top != ch && (top | 32) == (ch | 32)) {
                    stack.deleteCharAt(stack.length() - 1);
                    continue;
                }
            }
            stack.append(ch);
        }
        return stack.toString();
    }
}
