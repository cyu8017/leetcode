// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public long minCost(int[] nums, int[] costs) {
        int n = nums.length;
        long[] dp = new long[n];
        Arrays.fill(dp, Long.MAX_VALUE / 4);
        dp[0] = 0;
        var stack1 = new ArrayList<Integer>();
        var stack2 = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            while (stack1.size() > 0 && nums[stack1.get(stack1.size() - 1)] <= nums[i]) {
                int j = stack1.get(stack1.size() - 1); stack1.remove(stack1.size() - 1);
                dp[i] = Math.min(dp[i], dp[j] + costs[i]);
            }
            while (stack2.size() > 0 && nums[stack2.get(stack2.size() - 1)] > nums[i]) {
                int j = stack2.get(stack2.size() - 1); stack2.remove(stack2.size() - 1);
                dp[i] = Math.min(dp[i], dp[j] + costs[i]);
            }
            if (stack1.size() > 0) dp[i] = Math.min(dp[i], dp[stack1.get(stack1.size() - 1)] + costs[i]);
            if (stack2.size() > 0) dp[i] = Math.min(dp[i], dp[stack2.get(stack2.size() - 1)] + costs[i]);
            stack1.add(i);
            stack2.add(i);
        }
        return dp[n - 1];
    }
}
