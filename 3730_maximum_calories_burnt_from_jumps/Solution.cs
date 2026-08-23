// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

using System;

public class Solution {
    public long MaxCaloriesBurnt(int[] heights) {
        Array.Sort(heights);
        long ans = 0;
        int pre = 0, l = 0, r = heights.Length - 1;
        while (l < r) {
            long d1 = heights[r] - pre;
            ans += d1 * d1;
            long d2 = heights[l] - heights[r];
            ans += d2 * d2;
            pre = heights[l];
            l++;
            r--;
        }
        long d = heights[r] - pre;
        ans += d * d;
        return ans;
    }
}
