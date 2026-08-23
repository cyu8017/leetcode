// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

class Solution {
    public boolean isIdealPermutation(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (Math.abs(nums[i] - i) > 1) return false;
        }
        return true;
    }
}
