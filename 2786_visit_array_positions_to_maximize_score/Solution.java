// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

class Solution {
    public long maxScore(int[] nums, int x) {
        long NEG = -(1L << 60);
        long even = nums[0], odd = nums[0];
        if (nums[0] % 2 == 0) odd = NEG;
        else even = NEG;
        for (int i = 1; i < nums.length; i++) {
            long v = nums[i];
            if (nums[i] % 2 == 0) even = Math.max(even + v, odd + v - x);
            else odd = Math.max(odd + v, even + v - x);
        }
        return Math.max(even, odd);
    }
}
