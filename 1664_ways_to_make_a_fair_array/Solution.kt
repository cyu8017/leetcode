// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution {
    fun waysToMakeFair(nums: IntArray): Int {
        var te = 0
        var to = 0
        for (i in nums.indices) {
            if (i % 2 == 0) te += nums[i] else to += nums[i]
        }
        var le = 0
        var lo = 0
        var ans = 0
        for (i in nums.indices) {
            val x = nums[i]
            if (i % 2 == 1) to -= x else te -= x
            if (le + to == lo + te) ans++
            if (i % 2 == 1) lo += x else le += x
        }
        return ans
    }
}
