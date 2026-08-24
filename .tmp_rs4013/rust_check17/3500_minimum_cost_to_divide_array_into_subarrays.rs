struct Solution;
// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, cost: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut pn = vec![0i64; n + 1];
        let mut pc = vec![0i64; n + 1];
        for i in 0..n {
            pn[i + 1] = pn[i] + nums[i] as i64;
            pc[i + 1] = pc[i] + cost[i] as i64;
        }
        const INF: i64 = 1i64 << 62;
        let mut dp = vec![0i64; n + 1];
        for i in 0..n {
            dp[i] = INF;
        }
        for i in (0..n).rev() {
            for j in i..n {
                let cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k as i64 * (pc[n] - pc[i]) + dp[j + 1];
                if cand < dp[i] {
                    dp[i] = cand;
                }
            }
        }
        dp[0]
    }
}

fn main() {}
