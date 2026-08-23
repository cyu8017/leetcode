// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

public class Solution {
    public bool HasAlternatingBits(int n) {
        uint x = (uint)n ^ ((uint)n >> 1);
        return (x & (x + 1)) == 0;
    }
}
