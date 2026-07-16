// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

class Solution {
    fun verifyPreorder(preorder: IntArray): Boolean {
        var low = Long.MIN_VALUE
        val stack = ArrayDeque<Int>()

        for (value in preorder) {
            if (value < low) {
                return false
            }
            while (stack.isNotEmpty() && stack.last() < value) {
                low = stack.removeLast().toLong()
            }
            stack.addLast(value)
        }

        return true
    }
}
