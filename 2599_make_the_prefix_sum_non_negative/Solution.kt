// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

class Solution {
    fun makePrefSumNonNegative(nums: IntArray): Int {
        var h = PriorityQueue<Int>()
        var sum = 0
        var ans = 0
        for (x in nums) {
            sum += x
            if (x < 0) h.offer(x)
            if (sum < 0) {
                var worst = h.poll()
                sum -= worst
                ans = ans + 1
            }
        }
        return ans
    }
}
