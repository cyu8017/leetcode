// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution {
    fun minimumOperations(nums: IntArray): Int {
        val seen = HashSet<Int>()
        for (x in nums) if (x > 0) seen.add(x)
        return seen.size
    }
}
