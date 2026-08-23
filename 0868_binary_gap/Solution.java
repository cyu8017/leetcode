// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

class Solution {
    public int binaryGap(int n) {
        int last = -1, ans = 0, bit = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                if (last != -1) ans = Math.max(ans, bit - last);
                last = bit;
            }
            n >>= 1;
            bit++;
        }
        return ans;
    }
}
