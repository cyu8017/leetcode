// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

using System;

public class Solution {
    public bool PartitionArray(int[] nums, int k) {
        int n = nums.Length;
        if (n % k != 0) return false;
        int m = n / k;
        int mx = 0;
        foreach (int x in nums) mx = Math.Max(mx, x);
        int[] cnt = new int[mx + 1];
        foreach (int x in nums)
            if (++cnt[x] > m) return false;
        return true;
    }
}
