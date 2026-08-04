// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

class Solution {
    fun circularPermutation(n: Int, start: Int): List<Int> {
        val size = 1 shl n
        return List(size) { i -> start xor i xor (i shr 1) }
    }
}
