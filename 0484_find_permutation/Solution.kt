// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

class Solution {
    fun findPermutation(s: String): IntArray {
        val stack = ArrayDeque<Int>()
        val result = mutableListOf<Int>()
        stack.addLast(1)
        for (ch in s) {
            if (ch == 'I') {
                while (stack.isNotEmpty()) {
                    result.add(stack.removeLast())
                }
            }
            stack.addLast(stack.size + result.size + 1)
        }
        while (stack.isNotEmpty()) {
            result.add(stack.removeLast())
        }
        return result.toIntArray()
    }
}
