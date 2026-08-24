// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

impl Solution {
    pub fn binary_gap(mut n: i32) -> i32 {
        let mut last = -1;
        let mut ans = 0;
        let mut bit = 0;
        while n != 0 {
            if n & 1 != 0 {
                if last != -1 {
                    ans = ans.max(bit - last);
                }
                last = bit;
            }
            n >>= 1;
            bit += 1;
        }
        ans
    }
}
