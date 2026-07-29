// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution {
    fun prefixesDivBy5(nums: IntArray): List<Boolean> {
        val ans = ArrayList<Boolean>(nums.size)
        var rem = 0
        for (bit in nums) {
            rem = (rem * 2 + bit) % 5
            ans.add(rem == 0)
        }
        return ans
    }
}
