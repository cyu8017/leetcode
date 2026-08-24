// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution {
    fun rangeSum(nums: IntArray, n: Int, left: Int, right: Int): Int {
        val mod = 1_000_000_007
        val values = mutableListOf<Int>()
        for (i in 0 until n) {
            var total = 0
            for (j in i until n) {
                total += nums[j]
                values.add(total)
            }
        }
        values.sort()
        var sum = 0L
        for (i in left - 1 until right) {
            sum += values[i]
        }
        return (sum % mod).toInt()
    }
}
