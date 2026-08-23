// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution {
    public int maximumStrongPairXor(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++)
            for (int j = i; j < nums.length; j++) {
                int x = nums[i], y = nums[j];
                if (Math.abs(x - y) <= Math.min(x, y)) {
                    int xorr = x ^ y;
                    if (xorr > ans) ans = xorr;
                }
            }
        return ans;
    }
}
