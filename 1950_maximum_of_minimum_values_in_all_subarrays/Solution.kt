// LeetCode 1950
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

class Solution {
    fun findMaximums(nums: IntArray): IntArray {
        val n = nums.size
        val left = IntArray(n) { -1 }
        val right = IntArray(n) { n }
        val stack = ArrayDeque<Int>()
        for (i in nums.indices) {
            while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) stack.removeLast()
            left[i] = if (stack.isEmpty()) -1 else stack.last()
            stack.addLast(i)
        }
        stack.clear()
        for (i in n - 1 downTo 0) {
            while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) stack.removeLast()
            right[i] = if (stack.isEmpty()) n else stack.last()
            stack.addLast(i)
        }
        val ans = IntArray(n)
        for (i in nums.indices) {
            val length = right[i] - left[i] - 1
            ans[length - 1] = maxOf(ans[length - 1], nums[i])
        }
        for (i in n - 2 downTo 0) ans[i] = maxOf(ans[i], ans[i + 1])
        return ans
    }
}
