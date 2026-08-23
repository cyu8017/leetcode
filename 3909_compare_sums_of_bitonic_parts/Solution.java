// LeetCode 3909 - Compare Sums Of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

class Solution {
    public int compareBitonicSums(int[] nums) {
        long l = nums[0], r = 0;
        for (int x : nums) r += x;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > nums[i]) break;
            l += nums[i];
            r -= nums[i - 1];
        }
        if (l == r) return -1;
        if (l > r) return 0;
        return 1;
    }
}
