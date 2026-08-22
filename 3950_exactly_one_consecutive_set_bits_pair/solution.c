// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

#include <stdbool.h>

bool consecutiveSetBits(int n) {
    bool vis = false;
    int pre = 0;
    for (; n > 0; n >>= 1) {
        int cur = n & 1;
        if (pre == cur && cur == 1) {
            if (vis) return false;
            vis = true;
        }
        pre = cur;
    }
    return vis;
}
