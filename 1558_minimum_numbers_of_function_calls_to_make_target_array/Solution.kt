// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

class Solution {
    fun minOperations(nums: IntArray): Int {
        var adds = 0
        var maxBits = 0
        for (x in nums) {
            var bits = 0
            var t = x
            while (t > 0) {
                adds += t and 1
                bits++
                t = t shr 1
            }
            maxBits = maxOf(maxBits, bits - 1)
        }
        return adds + maxBits
    }
}
