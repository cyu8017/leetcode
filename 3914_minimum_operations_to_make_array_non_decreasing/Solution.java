// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

class Solution {
    public long minOperations(int[] nums) {
        long ans = 0;
        for (int i = 1; i < nums.length; i++) {
            ans += Math.max(0L, (long)nums[i - 1] - nums[i]);
        }
        return ans;
    }
}
