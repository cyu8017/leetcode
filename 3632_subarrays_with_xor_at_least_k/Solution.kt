// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

class Solution {
    fun subarraysWithXorAtLeastK(nums: IntArray, k: Int): Long {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var x = 0
            for (j in i until n) {
                x ^= nums[j]
                if (x >= k) ans++
            }
        }
        return ans
    }
}
