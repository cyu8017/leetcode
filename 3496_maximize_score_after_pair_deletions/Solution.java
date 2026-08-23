// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

class Solution {
    public int maximizeScore(int[] nums) {
        int n = nums.length;
        int total = 0;
        for (int x : nums) total += x;
        if (n % 2 == 1) {
            int mn = nums[0];
            for (int x : nums) if (x < mn) mn = x;
            return total - mn;
        }
        int mn = nums[0] + nums[1];
        for (int i = 0; i + 1 < n; i++) mn = Math.min(mn, nums[i] + nums[i + 1]);
        return total - mn;
    }
}
