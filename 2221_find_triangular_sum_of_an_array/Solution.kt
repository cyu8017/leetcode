// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution {

    fun triangularSum(nums: IntArray): Int {
        var _nums = nums

            while (_nums.size > 1) {
                var next = IntArray(_nums.size - 1)
                for (i in 0 until next.size) { next[i] = (_nums[i] + _nums[i + 1]) % 10 }
                _nums = next
            }
            return _nums[0]
    }

}
