// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        val n = nums.size
        if (n <= 2) return n
        var x = n
        var len = 0
        while (x != 0) {
            len++
            x = x shr 1
        }
        return 1 shl len
    }
}
