// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

class Solution {
    public long maxNumber(long n) {
        int len = 64 - Long.numberOfLeadingZeros(n);
        return (1L << (len - 1)) - 1;
    }
}
