// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

class Solution {
    public int missingNumber(int[] nums) {
        int length = nums.length;
        int expected = length * (length + 1) / 2;
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        return expected - total;
    }
}
