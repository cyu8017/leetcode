// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

public class Solution {
    public int[] GetMaximumXor(int[] nums, int maximumBit) {
        int limit = (1 << maximumBit) - 1;
        int current = 0;
        foreach (int num in nums) current ^= num;

        int[] result = new int[nums.Length];
        for (int i = nums.Length - 1; i >= 0; i--) {
            result[nums.Length - 1 - i] = current ^ limit;
            current ^= nums[i];
        }
        return result;
    }
}
