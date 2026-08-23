// LeetCode 2220 - Minimum Bit Flips to Convert Number
// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution {
    public int minBitFlips(int start, int goal) {
        int x = start ^ goal;
        int ans = 0;
        while (x > 0) {
            ans += x & 1;
            x >>= 1;
        }
        return ans;
    }
}
