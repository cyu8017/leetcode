// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

class Solution {
    fun semiOrderedPermutation(nums: IntArray): Int {
        val n = nums.size
        var p1 = 0
        var pn = 0
        for (i in 0 until n) {
            if (nums[i] == 1) p1 = i
            if (nums[i] == n) pn = i
        }
        var ans = p1 + (n - 1 - pn)
        if (p1 > pn) ans--
        return ans
    }
}
