// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution {
    fun maxSumTwoNoOverlap(nums: IntArray, firstLen: Int, secondLen: Int): Int {
        val prefix = IntArray(nums.size + 1)
        for (i in nums.indices) prefix[i + 1] = prefix[i] + nums[i]
        return maxOf(best(prefix, firstLen, secondLen), best(prefix, secondLen, firstLen))
    }

    private fun best(prefix: IntArray, a: Int, b: Int): Int {
        var bestA = 0; var ans = 0
        for (i in a + b until prefix.size) {
            bestA = maxOf(bestA, prefix[i - b] - prefix[i - b - a])
            ans = maxOf(ans, bestA + prefix[i] - prefix[i - b])
        }
        return ans
    }
}
