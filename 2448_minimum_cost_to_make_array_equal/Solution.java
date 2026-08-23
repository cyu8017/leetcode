// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

import java.util.Arrays;

class Solution {
    public long minCost(int[] nums, int[] cost) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(nums[a], nums[b]));
        long totalCost = 0;
        for (int c : cost) totalCost += c;
        long pref = 0;
        int median = 0;
        for (int i : idx) {
            pref += cost[i];
            if (pref * 2 >= totalCost) {
                median = nums[i];
                break;
            }
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long diff = nums[i] - median;
            if (diff < 0) diff = -diff;
            ans += diff * cost[i];
        }
        return ans;
    }
}
