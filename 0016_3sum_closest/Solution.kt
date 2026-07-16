// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

import kotlin.math.abs

class Solution {
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        nums.sort()
        var closest = nums[0] + nums[1] + nums[2]

        for (i in 0 until nums.size - 2) {
            var left = i + 1
            var right = nums.size - 1
            while (left < right) {
                val total = nums[i] + nums[left] + nums[right]
                if (abs(total - target) < abs(closest - target)) {
                    closest = total
                }
                when {
                    total < target -> left++
                    total > target -> right--
                    else -> return total
                }
            }
        }

        return closest
    }
}
