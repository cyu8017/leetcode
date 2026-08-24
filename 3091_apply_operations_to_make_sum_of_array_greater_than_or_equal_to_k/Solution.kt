// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

class Solution {
    fun minOperations(k: Int): Int {
        var ans = k
        for (a in 0 until k) {
            var x = a + 1
            var b = (k + x - 1) / x - 1
            ans = minOf(ans, a + b)
        }
        return ans
    }
}
