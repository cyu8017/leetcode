// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution {
    fun maxDepth(s: String): Int {
        var depth = 0
        var ans = 0
        for (ch in s) {
            if (ch == '(') {
                depth++
                ans = maxOf(ans, depth)
            } else if (ch == ')') {
                depth--
            }
        }
        return ans
    }
}
