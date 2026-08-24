// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

import java.util.ArrayDeque

class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        val window = ArrayDeque<Int>()
        val result = IntArray(nums.size - k + 1)
        var resultIndex = 0

        for (index in nums.indices) {
            while (window.isNotEmpty() && nums[window.last()] <= nums[index]) {
                window.removeLast()
            }
            window.addLast(index)
            if (window.first() <= index - k) {
                window.removeFirst()
            }
            if (index >= k - 1) {
                result[resultIndex++] = nums[window.first()]
            }
        }

        return result
    }
}
