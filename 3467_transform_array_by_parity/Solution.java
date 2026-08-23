// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

class Solution {
    public int[] transformArray(int[] nums) {
        for (int i = 0; i < nums.length; i++) nums[i] %= 2;
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                int t = nums[i]; nums[i] = nums[j]; nums[j] = t;
                j++;
            }
        }
        return nums;
    }
}
