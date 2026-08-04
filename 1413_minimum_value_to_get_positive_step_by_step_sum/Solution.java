// LeetCode 1413 - Minimum Value To Get Positive Step By Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution {
    public int minStartValue(int[] nums) {
        int prefix = 0, lowest = 0;
        for (int value : nums) { prefix += value; lowest = Math.min(lowest, prefix); }
        return 1 - lowest;
    }
}
