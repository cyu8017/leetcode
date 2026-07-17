// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

impl Solution {
    pub fn solve(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let block = (n as f64).sqrt() as usize + 1;
        let mut dp = vec![vec![0i64; n]; block];
        for step in 1..block {
            for i in (0..n).rev() {
                let next = if i + step < n { dp[step][i + step] } else { 0 };
                dp[step][i] = (nums[i] as i64 + next) % MOD;
            }
        }
        let mut ans = Vec::with_capacity(queries.len());
        for query in &queries {
            let start = query[0] as usize;
            let step = query[1] as usize;
            if step < block {
                ans.push(dp[step][start] as i32);
            } else {
                let mut total: i64 = 0;
                let mut i = start;
                while i < n {
                    total += nums[i] as i64;
                    i += step;
                }
                ans.push((total % MOD) as i32);
            }
        }
        ans
    }
}
