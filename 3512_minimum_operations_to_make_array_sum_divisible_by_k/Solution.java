// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution {
    public int minOperations(int[] nums, int k) {
        int ans = 0;
        for (int x : nums) ans = (ans + x) % k;
        return ans;
    }
}
