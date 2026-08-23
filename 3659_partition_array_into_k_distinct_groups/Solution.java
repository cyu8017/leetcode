// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

class Solution {
    public boolean partitionArray(int[] nums, int k) {
        int n = nums.length;
        if (n % k != 0) return false;
        int m = n / k;
        int mx = 0;
        for (int x : nums) mx = Math.max(mx, x);
        int[] cnt = new int[mx + 1];
        for (int x : nums)
            if (++cnt[x] > m) return false;
        return true;
    }
}
