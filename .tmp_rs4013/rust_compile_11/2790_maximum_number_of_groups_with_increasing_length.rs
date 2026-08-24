struct Solution;
fn main() {}

// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

impl Solution {
    pub fn max_increasing_groups(mut usage_limits: Vec<i32>) -> i32 {
        usage_limits.sort_unstable();
        let mut ans = 0i32;
        let mut sum = 0i64;
        for v in usage_limits {
            sum += v as i64;
            let need = (ans as i64 + 1) * (ans as i64 + 2) / 2;
            if sum >= need {
                ans += 1;
            }
        }
        ans
    }
}
