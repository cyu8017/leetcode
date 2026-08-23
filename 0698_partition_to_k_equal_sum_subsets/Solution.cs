// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

using System;

public class Solution {
    private int[] nums;
    private int[] buckets;
    private int target;

    private bool Dfs(int index) {
        if (index == nums.Length) return true;
        for (int i = 0; i < buckets.Length; i++) {
            if (buckets[i] + nums[index] > target) continue;
            buckets[i] += nums[index];
            if (Dfs(index + 1)) return true;
            buckets[i] -= nums[index];
            if (buckets[i] == 0) break;
        }
        return false;
    }

    public bool CanPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        foreach (int x in nums) total += x;
        if (total % k != 0) return false;
        target = total / k;
        this.nums = (int[])nums.Clone();
        Array.Sort(this.nums);
        Array.Reverse(this.nums);
        if (this.nums[0] > target) return false;
        buckets = new int[k];
        return Dfs(0);
    }
}
