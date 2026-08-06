// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution {
    fun longestSubarray(nums: IntArray, limit: Int): Int {
        val low = ArrayDeque<Int>()
        val high = ArrayDeque<Int>()
        var left = 0
        var answer = 0
        for (right in nums.indices) {
            val value = nums[right]
            while (low.isNotEmpty() && nums[low.last()] > value) low.removeLast()
            while (high.isNotEmpty() && nums[high.last()] < value) high.removeLast()
            low.add(right)
            high.add(right)
            while (nums[high.first()] - nums[low.first()] > limit) {
                left++
                if (low.first() < left) low.removeFirst()
                if (high.first() < left) high.removeFirst()
            }
            answer = maxOf(answer, right - left + 1)
        }
        return answer
    }
}
