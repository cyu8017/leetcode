// LeetCode 0312 - Burst Balloons

// https://leetcode.com/problems/burst-balloons/



class Solution {

    fun maxCoins(nums: IntArray): Int {

        val balloons = IntArray(nums.size + 2)

        balloons[0] = 1

        balloons[balloons.size - 1] = 1

        for (index in nums.indices) {

            balloons[index + 1] = nums[index]

        }



        val size = balloons.size

        val dp = Array(size) { IntArray(size) }

        for (length in 3..size) {

            for (left in 0..size - length) {

                val right = left + length - 1

                for (mid in left + 1 until right) {

                    val coins = dp[left][mid] + dp[mid][right] +

                        balloons[left] * balloons[mid] * balloons[right]

                    dp[left][right] = maxOf(dp[left][right], coins)

                }

            }

        }

        return dp[0][size - 1]

    }

}

