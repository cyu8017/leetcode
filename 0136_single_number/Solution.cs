// LeetCode 0136 - Single Number
// https://leetcode.com/problems/single-number/

public class Solution {
    public int SingleNumber(int[] nums) {
        int result = 0;
        foreach (int num in nums) result ^= num;
        return result;
    }
}
