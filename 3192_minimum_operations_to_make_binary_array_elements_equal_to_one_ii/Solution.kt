// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

class Solution {
    fun minOperations(nums: IntArray): Int {
        var ans = 0
        var v = 0
        for (raw in nums) {
            var x = raw ^ v
            if (x == 0) { v ^= 1; ans++; }
        }
        return ans
    }
}
