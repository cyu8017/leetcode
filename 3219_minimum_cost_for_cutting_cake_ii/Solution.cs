// LeetCode 3219 - Minimum Cost for Cutting Cake II
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

using System;

public class Solution {
    public long MinimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        Array.Sort(horizontalCut); Array.Reverse(horizontalCut);
        Array.Sort(verticalCut); Array.Reverse(verticalCut);
        int i = 0, j = 0, h = 1, v = 1;
        long ans = 0;
        while (i < m - 1 || j < n - 1) {
            if (j == n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
                ans += (long)horizontalCut[i] * v;
                h++; i++;
            } else {
                ans += (long)verticalCut[j] * h;
                v++; j++;
            }
        }
        return ans;
    }
}
