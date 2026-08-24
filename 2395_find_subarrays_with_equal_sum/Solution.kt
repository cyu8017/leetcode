// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution {
    fun findSubarrays(nums: IntArray): Boolean {
        val seen = HashSet<Int>()
        for (i in 0 until nums.size - 1) {
            val s = nums[i] + nums[i + 1]
            if (s in seen) return true
            seen.add(s)
        }
        return false
    }
}
