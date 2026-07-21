// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

class Solution {
    fun distinctNumbers(nums: IntArray, k: Int): IntArray {
        val counts = HashMap<Int, Int>()
        for (i in 0 until k) {
            counts[nums[i]] = counts.getOrDefault(nums[i], 0) + 1
        }
        val result = IntArray(nums.size - k + 1)
        result[0] = counts.size
        var left = 0
        var ri = 1
        for (right in k until nums.size) {
            counts[nums[right]] = counts.getOrDefault(nums[right], 0) + 1
            val outgoing = nums[left]
            val c = counts[outgoing]!! - 1
            if (c == 0) counts.remove(outgoing) else counts[outgoing] = c
            left++
            result[ri++] = counts.size
        }
        return result
    }
}
