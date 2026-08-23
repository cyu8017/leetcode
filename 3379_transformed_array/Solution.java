// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int j = ((i + nums[i]) % n + n) % n;
            ans[i] = nums[j];
        }
        return ans;
    }
}
