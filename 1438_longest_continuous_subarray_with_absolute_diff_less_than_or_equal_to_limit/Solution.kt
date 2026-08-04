// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution {
    fun longestSubarray(nums: IntArray, limit: Int): Int {
        val maxq = ArrayDeque<Int>()
        val minq = ArrayDeque<Int>()
        var left = 0
        var answer = 0
        for (right in nums.indices) {
            while (maxq.isNotEmpty() && nums[maxq.last()] < nums[right]) maxq.removeLast()
            while (minq.isNotEmpty() && nums[minq.last()] > nums[right]) minq.removeLast()
            maxq.addLast(right)
            minq.addLast(right)
            while (nums[maxq.first()] - nums[minq.first()] > limit) {
                if (maxq.first() == left) maxq.removeFirst()
                if (minq.first() == left) minq.removeFirst()
                left++
            }
            answer = maxOf(answer, right - left + 1)
        }
        return answer
    }
}
