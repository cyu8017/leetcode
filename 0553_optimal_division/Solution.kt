// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/


class Solution {
    fun optimalDivision(nums: IntArray): String {
        if (nums.size == 1) return nums[0].toString()
        if (nums.size == 2) return nums[0].toString() + "/" + nums[1].toString()
        val sb = StringBuilder()
        sb.append(nums[0]).append("/(")
        for (i in 1 until nums.size) {
            if (i > 1) sb.append('/')
            sb.append(nums[i])
        }
        sb.append(')')
        return sb.toString()
    }
}
