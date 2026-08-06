// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

impl Solution {
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut used = vec![false; n];
        let mut dist = vec![i32::MAX; n];
        dist[0] = 0;
        let mut answer = 0;
        for _ in 0..n {
            let mut u = 0;
            let mut best = i32::MAX;
            for i in 0..n {
                if !used[i] && dist[i] < best {
                    best = dist[i];
                    u = i;
                }
            }
            used[u] = true;
            answer += dist[u];
            for v in 0..n {
                if !used[v] {
                    let d = (points[u][0] - points[v][0]).abs()
                        + (points[u][1] - points[v][1]).abs();
                    dist[v] = dist[v].min(d);
                }
            }
        }
        answer
    }
}
