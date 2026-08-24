// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

class Solution {
    fun minimumCost(nums: IntArray): Int {
        var a = nums[0]
        var b = 100
        var c = 100
        for (i in 1 until nums.size) {
            var x = nums[i]
            if (x < b) {
                c = b
                b = x
            } else if (x < c) {
                c = x
            }
        }
        return a + b + c
    }
}
