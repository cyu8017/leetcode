// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/


class Solution {
    fun findErrorNums(nums: IntArray): IntArray {
        val seen = BooleanArray(nums.size + 1)
        var dup = 0
        var sum = 0
        for (num in nums) {
            if (seen[num]) dup = num
            seen[num] = true
            sum += num
        }
        val n = nums.size
        val missing = n * (n + 1) / 2 - (sum - dup)
        return intArrayOf(dup, missing)
    }
}
