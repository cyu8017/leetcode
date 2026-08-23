// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;
        for (int i = 0; i + 1 < n; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        int[] ans = new int[n];
        int j = 0;
        for (int x : nums) if (x != 0) ans[j++] = x;
        return ans;
    }
}
