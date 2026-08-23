// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution {
    public int minOperations(int[] nums, int k) {
        int ans = 0;
        for (int x : nums) if (x < k) ans++;
        return ans;
    }
}
