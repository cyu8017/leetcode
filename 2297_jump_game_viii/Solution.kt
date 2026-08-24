// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

class Solution {

    fun minCost(nums: IntArray, costs: IntArray): Long {

            var n = nums.size
            var dp = LongArray(n)
            dp.fill(Long.MAX_VALUE / 4)
            dp[0] = 0
            var stack1 = ArrayList<Int>()
            var stack2 = ArrayList<Int>()
            for (i in 0 until n) {
                while (stack1.size > 0 && nums[stack1[stack1.size - 1]] <= nums[i]) {
                    var j = stack1[stack1.size - 1]; stack1.removeAt(stack1.size - 1)
                    dp[i] = minOf(dp[i], dp[j] + costs[i])
                }
                while (stack2.size > 0 && nums[stack2[stack2.size - 1]] > nums[i]) {
                    var j = stack2[stack2.size - 1]; stack2.removeAt(stack2.size - 1)
                    dp[i] = minOf(dp[i], dp[j] + costs[i])
                }
                if (stack1.size > 0) dp[i] = minOf(dp[i], dp[stack1[stack1.size - 1]] + costs[i])
                if (stack2.size > 0) dp[i] = minOf(dp[i], dp[stack2[stack2.size - 1]] + costs[i])
                stack1.add(i)
                stack2.add(i)
            }
            return dp[n - 1]

    }

}
