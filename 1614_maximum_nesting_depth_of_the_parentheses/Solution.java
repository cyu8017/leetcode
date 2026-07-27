// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution {
    public int maxDepth(String s) {
        int depth = 0, ans = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                depth++;
                ans = Math.max(ans, depth);
            } else if (ch == ')') {
                depth--;
            }
        }
        return ans;
    }
}
