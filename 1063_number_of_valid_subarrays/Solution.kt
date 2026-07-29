// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

class Solution {
    fun validSubarrays(nums: IntArray): Int {
        val stack = ArrayDeque<Int>()
        var ans = 0
        for (i in nums.indices) {
            while (stack.isNotEmpty() && nums[stack.first()] > nums[i]) {
                val j = stack.removeFirst()
                ans += i - j
            }
            stack.addFirst(i)
        }
        while (stack.isNotEmpty()) {
            val j = stack.removeFirst()
            ans += nums.size - j
        }
        return ans
    }
}
