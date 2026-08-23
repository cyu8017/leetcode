// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/
var consecutiveSetBits = function(n) {
        let vis = false;
        for (let pre = 0; n > 0; n >>= 1) {
            let cur = n & 1;
            if (pre == cur && cur == 1) {
                if (vis) return false;
                vis = true;
            }
            pre = cur;
        }
        return vis;
    
};
