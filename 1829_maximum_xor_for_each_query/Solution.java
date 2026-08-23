// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int limit = (1 << maximumBit) - 1;
        int current = 0;
        for (int num : nums) {
            current ^= num;
        }

        int[] result = new int[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            result[nums.length - 1 - i] = current ^ limit;
            current ^= nums[i];
        }
        return result;
    }
}
