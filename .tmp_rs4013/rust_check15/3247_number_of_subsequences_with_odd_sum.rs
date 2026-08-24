struct Solution;
// LeetCode 3247 - Number of Subsequences with Odd Sum
// https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

impl Solution {
    pub fn subsequence_count(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut f = [0, 0];
        for x in nums {
            let mut g = [0, 0];
            if x % 2 == 1 {
                g[0] = (f[0] + f[1]) % MOD;
                g[1] = (f[0] + f[1] + 1) % MOD;
            } else {
                g[0] = (f[0] + f[0] + 1) % MOD;
                g[1] = (f[1] + f[1]) % MOD;
            }
            f = g;
        }
        f[1]
    }
}

fn main() {}
