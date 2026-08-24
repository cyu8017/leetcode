struct Solution;
fn main() {}

// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, x: i32) -> i64 {
        let n = nums.len();
        let mut best = nums.clone();
        let mut ans: i64 = nums.iter().map(|&v| v as i64).sum();
        for rot in 1..n {
            let mut cur = rot as i64 * x as i64;
            for i in 0..n {
                best[i] = best[i].min(nums[(i + rot) % n]);
                cur += best[i] as i64;
            }
            ans = ans.min(cur);
        }
        ans
    }
}
