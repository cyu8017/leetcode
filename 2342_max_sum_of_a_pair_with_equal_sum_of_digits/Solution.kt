// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution {
    fun maximumSum(nums: IntArray): Int {
        val best = HashMap<Int, Int>()
        var ans = -1
        for (x in nums) {
            val ds = digitSum(x)
            val prev = best[ds]
            if (prev != null) {
                ans = maxOf(ans, prev + x)
                if (x > prev) best[ds] = x
            } else {
                best[ds] = x
            }
        }
        return ans
    }

    private fun digitSum(x: Int): Int {
        var v = x
        var s = 0
        while (v > 0) {
            s += v % 10
            v /= 10
        }
        return s
    }
}
