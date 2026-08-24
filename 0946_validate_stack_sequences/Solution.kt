// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

class Solution {
    fun validateStackSequences(pushed: IntArray, popped: IntArray): Boolean {
        var stack = mutableListOf()
        var j = 0
        for (x in pushed) {
            stack.add(x)
            while (!stack.isEmpty() && stack[stack.size - 1] == popped[j]) {
                stack.removeAt(stack.size - 1)
                j++
            }
        }
        return stack.isEmpty()
    }
}
