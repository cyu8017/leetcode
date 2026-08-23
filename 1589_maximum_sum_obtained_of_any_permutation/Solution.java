// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

import java.util.*;

class Solution {
    public int maxSumRangeQuery(int[] nums, int[][] requests) {
        final int MOD = 1_000_000_007;
        int[] diff = new int[nums.length + 1];
        for (int[] r : requests) {
            diff[r[0]]++;
            diff[r[1] + 1]--;
        }
        for (int i = 1; i < nums.length; i++) {
            diff[i] += diff[i - 1];
        }
        int[] freq = Arrays.copyOf(diff, nums.length);
        Arrays.sort(nums);
        Arrays.sort(freq);
        long ans = 0;
        for (int i = 0; i < nums.length; i++) {
            ans = (ans + 1L * nums[i] * freq[i]) % MOD;
        }
        return (int) ans;
    }
}
