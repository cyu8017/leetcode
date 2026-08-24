// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

class Solution {
    fun countOperationsToEmptyArray(nums: IntArray): Long {
        val n = nums.size
        val idx = Array(n) { it }
        idx.sortBy { nums[it] }
        var ans = n.toLong()
        for (i in 1 until n)
            if (idx[i] < idx[i - 1]) ans += (n - i).toLong()
        return ans
    }
}
