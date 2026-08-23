// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

class Solution {
    public int maxSumAfterOperation(int[] nums) {
        long noSquare = 0;
        long oneSquare = 0;
        long best = Long.MIN_VALUE;
        for (int value : nums) {
            long v = value;
            oneSquare = Math.max(Math.max(oneSquare + v, noSquare + v * v), v * v);
            noSquare = Math.max(noSquare + v, v);
            best = Math.max(best, oneSquare);
        }
        return (int) best;
    }
}
