// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

class Solution {
    fun maxSumMinProduct(nums: IntArray): Int {
        val mod = 1_000_000_007L
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in nums.indices) {
            prefix[i + 1] = prefix[i] + nums[i]
        }
        val leftBound = IntArray(n) { -1 }
        val stack = ArrayDeque<Int>()
        for (i in nums.indices) {
            while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) {
                stack.removeLast()
            }
            leftBound[i] = if (stack.isEmpty()) -1 else stack.last()
            stack.addLast(i)
        }
        val rightBound = IntArray(n) { n }
        stack.clear()
        for (i in n - 1 downTo 0) {
            while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) {
                stack.removeLast()
            }
            rightBound[i] = if (stack.isEmpty()) n else stack.last()
            stack.addLast(i)
        }
        var best = 0L
        for (i in nums.indices) {
            val total = prefix[rightBound[i]] - prefix[leftBound[i] + 1]
            best = maxOf(best, total * nums[i])
        }
        return (best % mod).toInt()
    }
}
