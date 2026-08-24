// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution {
    fun maxDepthAfterSplit(seq: String): IntArray {
        var depth = 0
        val ans = IntArray(seq.length)
        for (i in seq.indices) {
            if (seq[i] == '(') {
                ans[i] = depth % 2
                depth++
            } else {
                depth--
                ans[i] = depth % 2
            }
        }
        return ans
    }
}
