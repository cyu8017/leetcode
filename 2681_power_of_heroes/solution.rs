// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

impl Solution {
    pub fn sum_of_power(mut nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        nums.sort_unstable();
        let mut ans = 0i64;
        let mut s = 0i64;
        for x in nums {
            let x = x as i64;
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD;
            s = (s * 2 + x) % MOD;
        }
        ans as i32
    }
}
