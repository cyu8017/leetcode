// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

public class Solution {
    public bool ConsecutiveSetBits(int n) {
        bool vis = false;
        for (int pre = 0; n > 0; n >>= 1) {
            int cur = n & 1;
            if (pre == cur && cur == 1) {
                if (vis) return false;
                vis = true;
            }
            pre = cur;
        }
        return vis;
    }
}
