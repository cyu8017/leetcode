// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val seen = mutableSetOf<Int>()
        for (num in nums) {
            if (!seen.add(num)) {
                return true
            }
        }
        return false
    }
}
