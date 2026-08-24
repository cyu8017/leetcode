// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution {
    fun minOperations(nums: IntArray, numsDivide: IntArray): Int {
        var g = numsDivide[0]
        for (i in 1 until numsDivide.size) g = gcd(g, numsDivide[i])
        nums.sort()
        for (i in nums.indices) {
            if (g % nums[i] == 0) return i
        }
        return -1
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a; var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }
}
