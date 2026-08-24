// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

impl Solution {
    pub fn knight_dialer(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let moves = [
            vec![4, 6],
            vec![6, 8],
            vec![7, 9],
            vec![4, 8],
            vec![0, 3, 9],
            vec![],
            vec![0, 1, 7],
            vec![2, 6],
            vec![1, 3],
            vec![2, 4],
        ];
        let mut dp = vec![1i64; 10];
        for _ in 0..n - 1 {
            let mut ndp = vec![0i64; 10];
            for i in 0..10 {
                for &j in &moves[i] {
                    ndp[j] = (ndp[j] + dp[i]) % MOD;
                }
            }
            dp = ndp;
        }
        (dp.iter().sum::<i64>() % MOD) as i32
    }
}
