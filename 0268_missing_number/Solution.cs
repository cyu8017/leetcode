// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

public class Solution {
    public int MissingNumber(int[] nums) {
        int length = nums.Length;
        int expected = length * (length + 1) / 2;
        int total = 0;
        foreach (int num in nums) {
            total += num;
        }
        return expected - total;
    }
}
