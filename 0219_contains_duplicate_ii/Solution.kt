// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        val lastIndex = mutableMapOf<Int, Int>()
        for (i in nums.indices) {
            val prev = lastIndex[nums[i]]
            if (prev != null && i - prev <= k) {
                return true
            }
            lastIndex[nums[i]] = i
        }
        return false
    }
}
