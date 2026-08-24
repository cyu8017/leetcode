// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/


class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {
        val counts = HashMap<Int, Int>()
        counts[0] = 1
        var prefix = 0
        var answer = 0
        for (num in nums) {
            prefix += num
            answer += counts.getOrDefault(prefix - k, 0)
            counts[prefix] = counts.getOrDefault(prefix, 0) + 1
        }
        return answer
    }
}
