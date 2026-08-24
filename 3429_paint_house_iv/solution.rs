// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

impl Solution {
    pub fn min_cost(n: i32, cost: Vec<Vec<i32>>) -> i64 {
        const INF: i64 = 1i64 << 60;
        let m = n as usize / 2;
        let mut dp = [[INF; 3]; 3];
        for a in 0..3 {
            for b in 0..3 {
                dp[a][b] = if a == b {
                    INF
                } else {
                    cost[0][a] as i64 + cost[n as usize - 1][b] as i64
                };
            }
        }
        for i in 1..m {
            let mut ndp = [[INF; 3]; 3];
            for pa in 0..3 {
                for pb in 0..3 {
                    if dp[pa][pb] >= INF {
                        continue;
                    }
                    for a in 0..3 {
                        if a == pa {
                            continue;
                        }
                        for b in 0..3 {
                            if b == pb || a == b {
                                continue;
                            }
                            let v = dp[pa][pb] + cost[i][a] as i64 + cost[n as usize - 1 - i][b] as i64;
                            if v < ndp[a][b] {
                                ndp[a][b] = v;
                            }
                        }
                    }
                }
            }
            dp = ndp;
        }
        let mut ans = INF;
        for a in 0..3 {
            for b in 0..3 {
                if dp[a][b] < ans {
                    ans = dp[a][b];
                }
            }
        }
        ans
    }
}
