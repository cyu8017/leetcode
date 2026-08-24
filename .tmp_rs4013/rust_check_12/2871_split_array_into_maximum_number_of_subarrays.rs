struct Solution;
// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

impl Solution {
    pub fn max_subarrays(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut cur = -1i32;
        for v in nums {
            if cur == -1 {
                cur = v;
            } else {
                cur &= v;
            }
            if cur == 0 {
                ans += 1;
                cur = -1;
            }
        }
        if ans == 0 { 1 } else { ans }
    }
}

fn main() {}
