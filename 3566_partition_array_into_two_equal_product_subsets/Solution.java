// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

class Solution {
    public boolean checkEqualPartitions(int[] nums, long target) {
        int n = nums.length;
        for (int i = 0; i < (1 << n); i++) {
            long x = 1, y = 1;
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) != 0) x *= nums[j];
                else y *= nums[j];
                if (x > target || y > target) break;
            }
            if (x == target && y == target) return true;
        }
        return false;
    }
}
