// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

class Solution {

    fun maximumSumScore(nums: IntArray): Long {

            var total = 0; var pref = 0
            for (x in nums) total += x
            var ans = Long.MIN_VALUE
            for (x in nums) {
                pref += x
                ans = maxOf(ans, maxOf(pref, total - pref + x))
            }
            return ans

    }

}
