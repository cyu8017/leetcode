// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

public class Solution {
    public long MaxNumber(long n) {
        int len = 64 - LeadingZeroCount((ulong)n);
        return (1L << (len - 1)) - 1;
    }

    static int LeadingZeroCount(ulong x) {
        if (x == 0) return 64;
        int c = 0;
        if ((x >> 32) == 0) { c += 32; x <<= 32; }
        if ((x >> 48) == 0) { c += 16; x <<= 16; }
        if ((x >> 56) == 0) { c += 8; x <<= 8; }
        if ((x >> 60) == 0) { c += 4; x <<= 4; }
        if ((x >> 62) == 0) { c += 2; x <<= 2; }
        if ((x >> 63) == 0) c += 1;
        return c;
    }
}
