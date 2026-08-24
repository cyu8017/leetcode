// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

class Solution {
    fun numberGame(nums: IntArray): IntArray {
        nums.sort()
        var i = 0
        while (i + 1 < nums.size) {
            var t = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = t
            i += 2
        }
        return nums
    }
}
