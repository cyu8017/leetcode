// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution {
    fun maximumValueSum(nums: IntArray, k: Int, edges: Array<IntArray>): Long {
        var f0 = 0
        var f1 = -0x3f3f3f3fL
        for (x in nums) {
            var nf0 = maxOf(f0 + x, f1 + (x ^ k))
            var nf1 = maxOf(f1 + x, f0 + (x ^ k))
            f0 = nf0
            f1 = nf1
        }
        return f0
    }
}
