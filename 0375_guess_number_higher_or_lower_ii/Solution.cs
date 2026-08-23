// LeetCode 0375 - Guess Number Higher or Lower II

// https://leetcode.com/problems/guess-number-higher-or-lower-ii/



public class Solution {

    public int GetMoneyAmount(int n) {

        int[,] dp = new int[n + 2, n + 2];



        for (int length = 2; length <= n; length++) {

            for (int left = 1; left <= n - length + 1; left++) {

                int right = left + length - 1;

                dp[left, right] = int.MaxValue;

                for (int guess = left; guess < right; guess++) {

                    int cost = guess + System.Math.Max(dp[left, guess - 1], dp[guess + 1, right]);

                    dp[left, right] = System.Math.Min(dp[left, right], cost);

                }

            }

        }



        return dp[1, n];

    }

}
