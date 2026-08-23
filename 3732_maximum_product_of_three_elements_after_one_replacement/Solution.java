// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

import java.util.Arrays;

class Solution {
    public long maxProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        long a = nums[0], b = nums[1], c = nums[n - 2], d = nums[n - 1];
        final long x = 100000;
        return Math.max(Math.max(a * b * x, c * d * x), -a * d * x);
    }
}
