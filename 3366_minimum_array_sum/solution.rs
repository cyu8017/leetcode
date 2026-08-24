// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

impl Solution {
    pub fn min_array_sum(nums: Vec<i32>, k: i32, op1: i32, op2: i32) -> i32 {
        const INF: i64 = 10i64.pow(18);
        let op1 = op1 as usize;
        let op2 = op2 as usize;
        let mut dp = vec![vec![INF; op2 + 1]; op1 + 1];
        dp[0][0] = 0;
        for x in nums {
            let mut ndp = vec![vec![INF; op2 + 1]; op1 + 1];
            for a in 0..=op1 {
                for b in 0..=op2 {
                    if dp[a][b] == INF {
                        continue;
                    }
                    let mut cand = vec![(a, b, x)];
                    if a < op1 {
                        cand.push((a + 1, b, (x + 1) / 2));
                    }
                    if b < op2 && x >= k {
                        cand.push((a, b + 1, x - k));
                    }
                    if a < op1 && b < op2 {
                        let v1 = (x + 1) / 2;
                        if v1 >= k {
                            cand.push((a + 1, b + 1, v1 - k));
                        }
                        if x >= k {
                            cand.push((a + 1, b + 1, (x - k + 1) / 2));
                        }
                    }
                    for (na, nb, v) in cand {
                        if dp[a][b] + (v as i64) < ndp[na][nb] {
                            ndp[na][nb] = dp[a][b] + v as i64;
                        }
                    }
                }
            }
            dp = ndp;
        }
        let mut ans = INF;
        for a in 0..=op1 {
            for b in 0..=op2 {
                if dp[a][b] < ans {
                    ans = dp[a][b];
                }
            }
        }
        ans as i32
    }
}
