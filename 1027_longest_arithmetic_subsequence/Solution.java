// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestArithSeqLength(int[] nums) {
        @SuppressWarnings("unchecked")
        Map<Integer, Integer>[] dp = new HashMap[nums.length];
        int ans = 1;
        for (int j = 1; j < nums.length; j++) {
            dp[j] = new HashMap<>();
            for (int i = 0; i < j; i++) {
                int d = nums[j] - nums[i];
                int prev = 1;
                if (dp[i] != null) prev = dp[i].getOrDefault(d, 1);
                int cur = prev + 1;
                dp[j].put(d, cur);
                ans = Math.max(ans, cur);
            }
        }
        return ans;
    }
}
