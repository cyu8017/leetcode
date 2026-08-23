// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

import java.util.Arrays;

class Solution {
    public int maximumStrongPairXor(int[] nums) {
        Arrays.sort(nums);
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            for (int j = i; j < nums.length && nums[j] <= 2 * x; j++) {
                int xorr = x ^ nums[j];
                if (xorr > ans) ans = xorr;
            }
        }
        return ans;
    }
}
