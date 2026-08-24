// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

impl Solution {
    pub fn cheapest_jump(coins: Vec<i32>, max_jump: i32) -> Vec<i32> {
        let n = coins.len();
        if coins[n - 1] == -1 {
            return Vec::new();
        }
        let inf = i64::MAX / 4;
        let mut cost = vec![inf; n];
        let mut nxt = vec![-1i32; n];
        cost[n - 1] = coins[n - 1] as i64;
        for i in (0..n - 1).rev() {
            if coins[i] == -1 {
                continue;
            }
            for jump in 1..=max_jump {
                let j = i + jump as usize;
                if j >= n {
                    break;
                }
                if cost[j] == inf {
                    continue;
                }
                let candidate = coins[i] as i64 + cost[j];
                if candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || (j as i32) < nxt[i])) {
                    cost[i] = candidate;
                    nxt[i] = j as i32;
                }
            }
        }
        if cost[0] == inf {
            return Vec::new();
        }
        let mut path = vec![1];
        let mut i = 0;
        while i != n - 1 {
            i = nxt[i] as usize;
            path.push(i as i32 + 1);
        }
        path
    }
}
