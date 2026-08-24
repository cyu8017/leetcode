// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = 0i64;
        let mut cur = k as i64;
        for &x0 in &nums {
            let x = x0 as i64;
            let diff = x - cur;
            if diff > 0 {
                let m = (diff + k as i64 - 1) / k as i64;
                cur += m * k as i64;
                cnt += m;
            }
            cur -= x;
        }
        cnt %= MOD;
        ((cnt + 1) * cnt / 2 % MOD) as i32
    }
}
