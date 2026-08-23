// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

using System;

public class Solution {
    public int BinaryGap(int n) {
        int last = -1, ans = 0, bit = 0;
        while (n != 0) {
            if ((n & 1) != 0) {
                if (last != -1) ans = Math.Max(ans, bit - last);
                last = bit;
            }
            n >>= 1;
            bit++;
        }
        return ans;
    }
}
