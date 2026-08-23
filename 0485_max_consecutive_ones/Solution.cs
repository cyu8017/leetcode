// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int best = 0;
        int current = 0;
        foreach (int num in nums) {
            if (num == 1) {
                current += 1;
                best = Math.Max(best, current);
            } else {
                current = 0;
            }
        }
        return best;
    }
}
