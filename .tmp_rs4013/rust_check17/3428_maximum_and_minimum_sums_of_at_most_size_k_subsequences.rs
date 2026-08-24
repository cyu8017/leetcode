struct Solution;
// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

impl Solution {
    pub fn min_max_sums(mut nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        nums.sort_unstable();
        let n = nums.len();
        let k = k as usize;
        let mut c = vec![vec![0; k]; n + 1];
        for i in 0..=n {
            c[i][0] = 1;
            let mut j = 1;
            while j < k && j <= i {
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD;
                j += 1;
            }
        }
        let mut ans = 0;
        for i in 0..n {
            let mut ways_max = 0;
            let mut j = 0;
            while j < k && j <= i {
                ways_max = (ways_max + c[i][j]) % MOD;
                j += 1;
            }
            let mut ways_min = 0;
            let right = n - i - 1;
            j = 0;
            while j < k && j <= right {
                ways_min = (ways_min + c[right][j]) % MOD;
                j += 1;
            }
            ans = ((ans as i64
                + nums[i] as i64 * ways_max as i64 % MOD as i64
                + nums[i] as i64 * ways_min as i64 % MOD as i64)
                % MOD as i64) as i32;
        }
        ans
    }
}

fn main() {}
