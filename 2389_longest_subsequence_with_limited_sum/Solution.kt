// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution {
    fun answerQueries(nums: IntArray, queries: IntArray): IntArray {
        nums.sort()
        for (i in 1 until nums.size) nums[i] += nums[i - 1]
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            var lo = 0
            var hi = nums.size
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (nums[mid] <= queries[i]) lo = mid + 1 else hi = mid
            }
            ans[i] = lo
        }
        return ans
    }
}
