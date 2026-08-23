// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

import java.util.*;

class Solution {
    private int[] nums;
    private int[] buckets;
    private int target;

    private boolean dfs(int index) {
        if (index == nums.length) return true;
        for (int i = 0; i < buckets.length; i++) {
            if (buckets[i] + nums[index] > target) continue;
            buckets[i] += nums[index];
            if (dfs(index + 1)) return true;
            buckets[i] -= nums[index];
            if (buckets[i] == 0) break;
        }
        return false;
    }

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int x : nums) total += x;
        if (total % k != 0) return false;
        target = total / k;
        this.nums = nums.clone();
        Arrays.sort(this.nums);
        for (int i = 0, j = this.nums.length - 1; i < j; i++, j--) {
            int tmp = this.nums[i];
            this.nums[i] = this.nums[j];
            this.nums[j] = tmp;
        }
        if (this.nums[0] > target) return false;
        buckets = new int[k];
        return dfs(0);
    }
}
