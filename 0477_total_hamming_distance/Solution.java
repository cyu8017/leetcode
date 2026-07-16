// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

class Solution {
    public int totalHammingDistance(int[] nums) {
        int total = 0;
        for (int bit = 0; bit < 32; bit++) {
            int zeros = 0;
            int ones = 0;
            for (int value : nums) {
                if ((value & (1 << bit)) != 0) {
                    ones++;
                } else {
                    zeros++;
                }
            }
            total += zeros * ones;
        }
        return total;
    }
}
