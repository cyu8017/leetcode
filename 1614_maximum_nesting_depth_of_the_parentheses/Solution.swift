// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution {
    func maxDepth(_ s: String) -> Int {
        var depth = 0, ans = 0
        for ch in s {
            if ch == "(" {
                depth += 1
                ans = max(ans, depth)
            } else if ch == ")" {
                depth -= 1
            }
        }
        return ans
    }
}
