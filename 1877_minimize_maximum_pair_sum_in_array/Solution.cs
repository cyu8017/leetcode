// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

public class Solution {
    public int MinPairSum(int[] nums) {
        Array.Sort(nums);
        int best = 0;
        for (int i = 0; i < nums.Length / 2; i++) {
            best = Math.Max(best, nums[i] + nums[nums.Length - 1 - i]);
        }
        return best;
    }
}
