// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

import java.util.Arrays;

class Solution {
    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = 1, start = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - start > k) { ans++; start = nums[i]; }
        }
        return ans;
    }
}
