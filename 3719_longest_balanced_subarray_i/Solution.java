// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestBalanced(int[] nums) {
        int n = nums.length, ans = 0;
        for (int i = 0; i < n; i++) {
            var vis = new HashSet<Integer>();
            int[] cnt = new int[2];
            for (int j = i; j < n; j++) {
                if (!vis.contains(nums[j])) {
                    vis.add(nums[j]);
                    cnt[nums[j] & 1]++;
                }
                if (cnt[0] == cnt[1]) ans = Math.max(ans, j - i + 1);
            }
        }
        return ans;
    }
}
