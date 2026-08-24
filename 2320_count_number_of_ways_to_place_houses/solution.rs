// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

impl Solution {
    pub fn count_house_placements(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut a = 1i64;
        let mut b = 1i64;
        for _ in 1..=n {
            let na = (a + b) % MOD;
            b = a;
            a = na;
        }
        let ways = (a + b) % MOD;
        (ways * ways % MOD) as i32
    }
}
