// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

impl Solution {
    pub fn minimum_possible_sum(n: i32, target: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as i64;
        let target = target as i64;
        let m = target / 2;
        if n <= m {
            return (n * (n + 1) / 2 % MOD) as i32;
        }
        let mut sum = m * (m + 1) / 2;
        let remain = n - m;
        sum += remain * target + remain * (remain - 1) / 2;
        (sum % MOD) as i32
    }
}
