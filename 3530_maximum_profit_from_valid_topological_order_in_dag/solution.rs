// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

impl Solution {
    fn pop(mut x: i32) -> i32 {
        let mut c = 0;
        while x > 0 {
            c += x & 1;
            x >>= 1;
        }
        c
    }

    pub fn max_profit(n: i32, edges: Vec<Vec<i32>>, score: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut need = vec![0i32; n];
        let mut dp = vec![-1i32; 1 << n];
        dp[0] = 0;
        for e in &edges {
            need[e[1] as usize] |= 1 << e[0];
        }
        for mask in 0..(1 << n) {
            if dp[mask] < 0 {
                continue;
            }
            let pos = Self::pop(mask as i32) + 1;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    continue;
                }
                if (mask as i32 & need[i]) == need[i] {
                    let nm = mask | (1 << i);
                    let v = dp[mask] + score[i] * pos;
                    if v > dp[nm] {
                        dp[nm] = v;
                    }
                }
            }
        }
        dp[(1 << n) - 1]
    }
}
