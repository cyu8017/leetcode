// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

public class Solution {
    public int MaxSumAfterOperation(int[] nums) {
        long noSquare = 0;
        long oneSquare = 0;
        long best = long.MinValue;
        foreach (int value in nums) {
            long v = value;
            oneSquare = Math.Max(Math.Max(oneSquare + v, noSquare + v * v), v * v);
            noSquare = Math.Max(noSquare + v, v);
            best = Math.Max(best, oneSquare);
        }
        return (int) best;
    }
}
