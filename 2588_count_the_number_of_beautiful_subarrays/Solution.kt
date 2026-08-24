// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

class Solution {
    fun beautifulSubarrays(nums: IntArray): Long {
        val freq = HashMap<Int, Int>()
        freq[0] = 1
        var xorv = 0
        var ans = 0L
        for (x in nums) {
            xorv = xorv xor x
            ans += freq.getOrDefault(xorv, 0)
            freq[xorv] = freq.getOrDefault(xorv, 0) + 1
        }
        return ans
    }
}
