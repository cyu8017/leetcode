// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

class Solution {
    fun grayCode(n: Int): List<Int> {
        val size = 1 shl n
        val result = ArrayList<Int>(size)
        for (i in 0 until size) {
            result.add(i xor (i shr 1))
        }
        return result
    }
}
