// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

impl Solution {
    pub fn min_cost(n: i32, mut cuts: Vec<i32>) -> i32 {
        cuts.sort_unstable();
        let mut points = Vec::with_capacity(cuts.len() + 2);
        points.push(0);
        points.extend(cuts);
        points.push(n);
        let size = points.len();
        let mut dp = vec![vec![0; size]; size];
        for width in 2..size {
            for left in 0..size - width {
                let right = left + width;
                let mut best = i32::MAX;
                for mid in left + 1..right {
                    best = best.min(dp[left][mid] + dp[mid][right]);
                }
                if best == i32::MAX {
                    best = 0;
                }
                if right > left + 1 {
                    best += points[right] - points[left];
                }
                dp[left][right] = best;
            }
        }
        dp[0][size - 1]
    }
}
