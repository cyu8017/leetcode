// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution {
    fun minPairSum(nums: IntArray): Int {
        nums.sort()
        var answer = 0
        val n = nums.size
        for (i in 0 until n / 2) {
            answer = maxOf(answer, nums[i] + nums[n - 1 - i])
        }
        return answer
    }
}
