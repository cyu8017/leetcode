// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution {
    fun countCompleteSubarrays(nums: IntArray): Int {
        val need = nums.toSet().size
        var ans = 0
        val n = nums.size
        for (i in 0 until n) {
            val seen = HashSet<Int>()
            for (j in i until n) {
                seen.add(nums[j])
                if (seen.size == need) {
                    ans += n - j
                    break
                }
            }
        }
        return ans
    }
}
