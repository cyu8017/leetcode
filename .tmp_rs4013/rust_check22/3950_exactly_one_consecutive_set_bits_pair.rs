struct Solution;
// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

impl Solution {
    pub fn consecutive_set_bits(mut n: i32) -> bool {
        let mut vis = false;
        let mut pre = 0;
        while n > 0 {
            let cur = n & 1;
            if pre == cur && cur == 1 {
                if vis {
                    return false;
                }
                vis = true;
            }
            pre = cur;
            n >>= 1;
        }
        vis
    }
}

fn main() {}
