// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int left = 0;
        int best = 0;
        int zeros = 0;
        for (int right = 0; right < nums.Length; right++) {
            if (nums[right] == 0) {
                zeros += 1;
            }
            while (zeros > 1) {
                if (nums[left] == 0) {
                    zeros -= 1;
                }
                left += 1;
            }
            best = Math.Max(best, right - left + 1);
        }
        return best;
    }
}
