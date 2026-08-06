// LeetCode 1411 - Number of Ways to Paint N × 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

impl Solution {
    pub fn num_of_ways(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut aba: i64 = 6;
        let mut abc: i64 = 6;
        for _ in 1..n {
            let na = (3 * aba + 2 * abc) % MOD;
            let nc = (2 * aba + 2 * abc) % MOD;
            aba = na;
            abc = nc;
        }
        ((aba + abc) % MOD) as i32
    }
}
