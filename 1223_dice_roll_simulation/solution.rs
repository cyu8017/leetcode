// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

impl Solution {
    pub fn die_simulator(n: i32, roll_max: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut dp: Vec<Vec<i32>> = (0..6)
            .map(|j| {
                let mut v = vec![0; roll_max[j] as usize + 1];
                v[1] = 1;
                v
            })
            .collect();
        for _ in 1..n {
            let totals: Vec<i32> = dp
                .iter()
                .map(|row| row.iter().fold(0, |a, &b| (a + b) % MOD))
                .collect();
            let all = totals.iter().fold(0, |a, &b| (a + b) % MOD);
            let mut nxt = vec![Vec::new(); 6];
            for j in 0..6 {
                nxt[j] = vec![0; dp[j].len()];
                nxt[j][1] = (all - totals[j] + MOD) % MOD;
                for run in 2..dp[j].len() {
                    nxt[j][run] = dp[j][run - 1];
                }
            }
            dp = nxt;
        }
        dp.iter()
            .flat_map(|row| row.iter())
            .fold(0, |a, &b| (a + b) % MOD)
    }
}
