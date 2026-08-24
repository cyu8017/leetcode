// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

impl Solution {
    pub fn max_profit(n: i32, present: Vec<i32>, future: Vec<i32>, hierarchy: Vec<Vec<i32>>, budget: i32) -> i32 {
        let n = n as usize;
        let budget = budget as usize;
        let mut g = vec![Vec::<usize>::new(); n + 1];
        for e in &hierarchy {
            g[e[0] as usize].push(e[1] as usize);
        }
        fn dfs(u: usize, budget: usize, g: &[Vec<usize>], present: &[i32], future: &[i32]) -> Vec<[i32; 2]> {
            let mut nxt = vec![[0i32; 2]; budget + 1];
            for &v in &g[u] {
                let fv = dfs(v, budget, g, present, future);
                for j in (0..=budget).rev() {
                    for jv in 0..=j {
                        for pre in 0..2 {
                            nxt[j][pre] = nxt[j][pre].max(nxt[j - jv][pre] + fv[jv][pre]);
                        }
                    }
                }
            }
            let mut f = vec![[0i32; 2]; budget + 1];
            let price = future[u - 1];
            for j in 0..=budget {
                for pre in 0..2 {
                    let cost = present[u - 1] / (pre as i32 + 1);
                    if j as i32 >= cost {
                        let buy_profit = nxt[j - cost as usize][1] + (price - cost);
                        f[j][pre] = nxt[j][0].max(buy_profit);
                    } else {
                        f[j][pre] = nxt[j][0];
                    }
                }
            }
            f
        }
        dfs(1, budget, &g, &present, &future)[budget][0]
    }
}
