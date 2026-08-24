struct Solution;
// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let mut ans = 1i64 << 62;
        for i in 0..=n.saturating_sub(k) {
            let mut sub = nums[i..i + k].to_vec();
            sub.sort_unstable();
            let med = sub[k / 2];
            let mut cost = 0i64;
            for x in sub {
                cost += (x - med).abs() as i64;
            }
            if cost < ans {
                ans = cost;
            }
        }
        ans
    }
}

fn main() {}
