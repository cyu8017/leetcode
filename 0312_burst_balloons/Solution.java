// LeetCode 0312 - Burst Balloons

// https://leetcode.com/problems/burst-balloons/



class Solution {

    public int maxCoins(int[] nums) {

        int size = nums.length + 2;

        int[] balloons = new int[size];

        balloons[0] = 1;

        balloons[size - 1] = 1;

        for (int index = 0; index < nums.length; index++) {

            balloons[index + 1] = nums[index];

        }



        int[][] dp = new int[size][size];

        for (int length = 3; length <= size; length++) {

            for (int left = 0; left <= size - length; left++) {

                int right = left + length - 1;

                for (int mid = left + 1; mid < right; mid++) {

                    int coins = dp[left][mid] + dp[mid][right]

                            + balloons[left] * balloons[mid] * balloons[right];

                    dp[left][right] = Math.max(dp[left][right], coins);

                }

            }

        }

        return dp[0][size - 1];

    }

}

