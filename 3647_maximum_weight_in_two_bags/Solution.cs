// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

using System;

public class Solution {
    public int MaxWeight(int[] weights, int w1, int w2) {
        int[][] f = new int[w1 + 1][];
        for (int j = 0; j <= w1; j++) f[j] = new int[w2 + 1];
        foreach (int x in weights) {
            for (int j = w1; j >= 0; j--) {
                for (int k = w2; k >= 0; k--) {
                    if (x <= j) f[j][k] = Math.Max(f[j][k], f[j - x][k] + x);
                    if (x <= k) f[j][k] = Math.Max(f[j][k], f[j][k - x] + x);
                }
            }
        }
        return f[w1][w2];
    }
}
