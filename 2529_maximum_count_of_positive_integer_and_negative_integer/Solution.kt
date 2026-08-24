// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution {
    fun maximumCount(nums: IntArray): Int {
        var pos = 0
        var neg = 0
        for (x in nums) {
            if (x > 0) { pos = pos + 1 }
            else if (x < 0) { neg = neg + 1 }
        }
        return maxOf(pos, neg)
    }
}
