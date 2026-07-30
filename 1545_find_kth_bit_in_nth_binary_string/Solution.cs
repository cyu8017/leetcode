// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

public class Solution {
    public char FindKthBit(int n, int k) {
        bool invert = false;
        int length = (1 << n) - 1;
        while (k != 1) {
            int middle = length / 2 + 1;
            if (k == middle) return invert ? '0' : '1';
            if (k > middle) {
                k = length - k + 1;
                invert = !invert;
            }
            length /= 2;
        }
        return invert ? '1' : '0';
    }
}
