// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

class Solution {
    public int minArrayLength(int[] nums, int k) {
        if (nums.length == 0) return 0;
        int ans = 1;
        long prod = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (prod <= k && nums[i] <= k && (nums[i] == 0 || prod <= k / nums[i])) {
                prod *= nums[i];
            } else {
                ans++;
                prod = nums[i];
            }
        }
        return ans;
    }
}
