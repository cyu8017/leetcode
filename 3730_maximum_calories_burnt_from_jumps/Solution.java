// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

import java.util.Arrays;

class Solution {
    public long maxCaloriesBurnt(int[] heights) {
        Arrays.sort(heights);
        long ans = 0;
        int pre = 0, l = 0, r = heights.length - 1;
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
