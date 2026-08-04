// LeetCode 1486 - XOR Operation in an Array
// https://leetcode.com/problems/xor-operation-in-an-array/

class Solution {
    fun xorOperation(n: Int, start: Int): Int {
        var ans = 0
        for (i in 0 until n) ans = ans xor (start + 2 * i)
        return ans
    }
}
