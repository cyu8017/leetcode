// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

impl Solution {
    pub fn min_side_jumps(obstacles: Vec<i32>) -> i32 {
        const INF: i32 = i32::MAX / 2;
        let mut dp = [1, 0, 1];

        for &obs in &obstacles {
            let blocked = [obs == 1, obs == 2, obs == 3];
            let mut ndp = [INF, INF, INF];
            for lane in 0..3 {
                if blocked[lane] {
                    continue;
                }
                for other in 0..3 {
                    if blocked[other] || dp[other] >= INF {
                        continue;
                    }
                    let cost = dp[other] + if lane != other { 1 } else { 0 };
                    ndp[lane] = ndp[lane].min(cost);
                }
            }
            dp = ndp;
        }

        *dp.iter().min().unwrap()
    }
}
