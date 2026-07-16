// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

class Solution {
    fun numberOfArithmeticSlices(nums: IntArray): Int {
        var total = 0
        val differences = Array(nums.size) { HashMap<Long, Int>() }

        for (index in nums.indices) {
            for (previous in 0 until index) {
                val diff = nums[index].toLong() - nums[previous]
                total += differences[previous].getOrDefault(diff, 0)
                differences[index][diff] =
                    differences[index].getOrDefault(diff, 0) +
                    differences[previous].getOrDefault(diff, 0) + 1
            }
        }

        return total
    }
}
