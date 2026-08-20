// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution {
    func maxDepthAfterSplit(_ seq: String) -> [Int] {
        var depth = 0
        var ans = [Int](repeating: 0, count: seq.count)
        for (i, ch) in seq.enumerated() {
            if ch == "(" {
                ans[i] = depth % 2
                depth += 1
            } else {
                depth -= 1
                ans[i] = depth % 2
            }
        }
        return ans
    }
}
