// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

public class Solution {
    public int MinChanges(int n, int k) {
        if ((n & k) != k) return -1;
        return PopCount(n ^ k);
    }

    static int PopCount(int x) {
        int c = 0;
        unchecked {
            uint u = (uint)x;
            while (u != 0) { c += (int)(u & 1); u >>= 1; }
        }
        return c;
    }
}
