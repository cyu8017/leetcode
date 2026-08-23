// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

using System;
using System.Linq;

public class Solution {
    public int MinCost(int n, int[] cuts) {
        var points = new int[cuts.Length + 2];
        points[0] = 0;
        Array.Sort(cuts);
        Array.Copy(cuts, 0, points, 1, cuts.Length);
        points[points.Length - 1] = n;
        int size = points.Length;
        int[,] dp = new int[size, size];
        for (int width = 2; width < size; width++) {
            for (int left = 0; left + width < size; left++) {
                int right = left + width;
                int best = int.MaxValue;
                for (int mid = left + 1; mid < right; mid++) {
                    best = Math.Min(best, dp[left, mid] + dp[mid, right]);
                }
                if (best == int.MaxValue) best = 0;
                if (right > left + 1) best += points[right] - points[left];
                dp[left, right] = best;
            }
        }
        return dp[0, size - 1];
    }
}
