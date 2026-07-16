// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int best = 0;
        int current = 0;
        for (int num : nums) {
            if (num == 1) {
                current += 1;
                best = Math.max(best, current);
            } else {
                current = 0;
            }
        }
        return best;
    }
}
