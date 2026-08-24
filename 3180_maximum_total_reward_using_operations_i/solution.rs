// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

impl Solution {
    pub fn max_total_reward(mut reward_values: Vec<i32>) -> i32 {
        reward_values.sort_unstable();
        let mx = *reward_values.last().unwrap();
        let mut f = vec![-1; (mx << 1) as usize];
        fn dfs(x: i32, reward_values: &[i32], f: &mut [i32]) -> i32 {
            if f[x as usize] != -1 {
                return f[x as usize];
            }
            let mut best = 0;
            for &v in reward_values.iter() {
                if v > x {
                    best = best.max(v + dfs(x + v, reward_values, f));
                }
            }
            f[x as usize] = best;
            best
        }
        dfs(0, &reward_values, &mut f)
    }
}
