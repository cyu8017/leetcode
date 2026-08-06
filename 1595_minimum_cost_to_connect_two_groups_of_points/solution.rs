// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

impl Solution {
    pub fn connect_two_groups(cost: Vec<Vec<i32>>) -> i32 {
        let m = cost.len();
        let n = cost[0].len();
        let full = 1 << n;
        let inf = 1_000_000_000;
        let mut dp = vec![inf; full];
        dp[0] = 0;
        for row in &cost {
            let mut nxt = vec![inf; full];
            for mask in 0..full {
                for (j, &value) in row.iter().enumerate() {
                    let new_mask = mask | (1 << j);
                    nxt[new_mask] = nxt[new_mask]
                        .min(dp[mask] + value)
                        .min(nxt[mask] + value);
                }
            }
            dp = nxt;
        }
        let minimum: Vec<i32> = (0..n)
            .map(|j| (0..m).map(|i| cost[i][j]).min().unwrap())
            .collect();
        (0..full)
            .map(|mask| {
                let mut extra = 0;
                for j in 0..n {
                    if mask >> j & 1 == 0 {
                        extra += minimum[j];
                    }
                }
                dp[mask] + extra
            })
            .min()
            .unwrap()
    }
}
