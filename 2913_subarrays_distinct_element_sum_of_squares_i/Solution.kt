// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution {
    fun sumCounts(nums: List<Int>): Int {
        val n = nums.size
        var ans = 0
        for (i in 0 until n) {
            val seen = HashSet<Int>()
            for (j in i until n) {
                seen.add(nums[j])
                val d = seen.size
                ans += d * d
            }
        }
        return ans
    }
}
