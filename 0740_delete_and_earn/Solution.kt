// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

class Solution {
    fun deleteAndEarn(nums: IntArray): Int {
        if (nums.size == 0) return 0
        var maxNum = 0
        for (num in nums) { maxNum = maxOf(maxNum, num) }
        var points = IntArray(maxNum + 1)
        for (num in nums) { points[num] += num }
        var take = 0
        var skip = 0
        for (value in points) {
            var newTake = skip + value
            var newSkip = maxOf(skip, take)
            take = newTake
            skip = newSkip
        }
        return maxOf(take, skip)
    }
}
