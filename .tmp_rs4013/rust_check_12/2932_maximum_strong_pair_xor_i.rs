struct Solution;
// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

impl Solution {
    pub fn maximum_strong_pair_xor(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i..nums.len() {
                let x = nums[i];
                let y = nums[j];
                if (x - y).abs() <= x.min(y) {
                    ans = ans.max(x ^ y);
                }
            }
        }
        ans
    }
}

fn main() {}
