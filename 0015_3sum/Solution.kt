// LeetCode 0015 - 3Sum
// https://leetcode.com/problems/3sum/

class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        val result = mutableListOf<List<Int>>()

        for (i in 0 until nums.size - 2) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue
            }

            var left = i + 1
            var right = nums.size - 1
            while (left < right) {
                val total = nums[i] + nums[left] + nums[right]
                when {
                    total == 0 -> {
                        result.add(listOf(nums[i], nums[left], nums[right]))
                        while (left < right && nums[left] == nums[left + 1]) {
                            left++
                        }
                        while (left < right && nums[right] == nums[right - 1]) {
                            right--
                        }
                        left++
                        right--
                    }
                    total < 0 -> left++
                    else -> right--
                }
            }
        }

        return result
    }
}
