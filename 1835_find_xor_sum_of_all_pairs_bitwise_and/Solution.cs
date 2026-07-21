// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

public class Solution {
    public int GetXORSum(int[] arr1, int[] arr2) {
        int xor1 = 0, xor2 = 0;
        foreach (int x in arr1) xor1 ^= x;
        foreach (int x in arr2) xor2 ^= x;
        return xor1 & xor2;
    }
}
