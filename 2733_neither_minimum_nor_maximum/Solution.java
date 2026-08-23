// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution {
    public int findNonMinOrMax(int[] nums) {
        if (nums.length < 3) return -1;
        int a = nums[0], b = nums[1], c = nums[2];
        return a + b + c - Math.max(a, Math.max(b, c)) - Math.min(a, Math.min(b, c));
    }
}
