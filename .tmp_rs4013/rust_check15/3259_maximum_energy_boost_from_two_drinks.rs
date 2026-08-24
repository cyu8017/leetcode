struct Solution;
// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

impl Solution {
    pub fn max_energy_boost(energy_drink_a: Vec<i32>, energy_drink_b: Vec<i32>) -> i64 {
        let n = energy_drink_a.len();
        let mut dp_a = vec![0i64; n];
        let mut dp_b = vec![0i64; n];
        dp_a[0] = energy_drink_a[0] as i64;
        dp_b[0] = energy_drink_b[0] as i64;
        if n == 1 {
            return dp_a[0].max(dp_b[0]);
        }
        dp_a[1] = energy_drink_a[1] as i64 + dp_a[0];
        dp_b[1] = energy_drink_b[1] as i64 + dp_b[0];
        for i in 2..n {
            dp_a[i] = energy_drink_a[i] as i64 + dp_a[i - 1].max(dp_b[i - 2]);
            dp_b[i] = energy_drink_b[i] as i64 + dp_b[i - 1].max(dp_a[i - 2]);
        }
        dp_a[n - 1].max(dp_b[n - 1])
    }
}

fn main() {}
