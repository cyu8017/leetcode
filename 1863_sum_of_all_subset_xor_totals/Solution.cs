// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

public class Solution {
    public int SubsetXORSum(int[] nums) {
        int bits = 0;
        foreach (int num in nums) {
            bits |= num;
        }
        int total = 0;
        for (int bit = 1; bit <= bits; bit <<= 1) {
            if ((bits & bit) != 0) {
                total += bit;
            }
        }
        return total << (nums.Length - 1);
    }
}
