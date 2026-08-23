// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

public class Solution {
    public int UniqueXorTriplets(int[] nums) {
        int n = nums.Length;
        if (n <= 2) return n;
        uint x = (uint)n;
        int len = 0;
        while (x != 0) { len++; x >>= 1; }
        return 1 << len;
    }
}
