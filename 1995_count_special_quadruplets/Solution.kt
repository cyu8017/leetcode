// LeetCode 1995
// https://leetcode.com/problems/count-special-quadruplets/

class Solution {
    fun countQuadruplets(nums: IntArray): Int {
        val n = nums.size
        var ans = 0
        for (a in 0 until n) for (b in a + 1 until n) for (c in b + 1 until n) {
            val s = nums[a] + nums[b] + nums[c]
            for (d in c + 1 until n) if (nums[d] == s) ans++
        }
        return ans
    }
}
