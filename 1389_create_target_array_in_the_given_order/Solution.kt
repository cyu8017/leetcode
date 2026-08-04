// LeetCode 1389 - Create Target Array in the Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution {
    fun createTargetArray(nums: IntArray, index: IntArray): IntArray {
        val out = mutableListOf<Int>()
        for (i in nums.indices) out.add(index[i], nums[i])
        return out.toIntArray()
    }
}
