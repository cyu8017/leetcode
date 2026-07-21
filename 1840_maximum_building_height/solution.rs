// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

impl Solution {
    pub fn max_building(n: i32, restrictions: Vec<Vec<i32>>) -> i32 {
        let mut points = vec![vec![1, 0]];
        let mut sorted = restrictions;
        sorted.sort_unstable();
        points.extend(sorted);
        if points.last().unwrap()[0] != n {
            points.push(vec![n, n - 1]);
        }

        for i in 1..points.len() {
            let prev_id = points[i - 1][0];
            let prev_height = points[i - 1][1];
            let curr_id = points[i][0];
            let curr_height = points[i][1];
            points[i][1] = curr_height.min(prev_height + curr_id - prev_id);
        }

        for i in (0..points.len() - 1).rev() {
            let next_id = points[i + 1][0];
            let next_height = points[i + 1][1];
            let curr_id = points[i][0];
            let curr_height = points[i][1];
            points[i][1] = curr_height.min(next_height + next_id - curr_id);
        }

        let mut best = points.iter().map(|p| p[1]).max().unwrap_or(0);
        for i in 0..points.len() - 1 {
            let id1 = points[i][0];
            let h1 = points[i][1];
            let id2 = points[i + 1][0];
            let h2 = points[i + 1][1];
            best = best.max((h1 + h2 + id2 - id1) / 2);
        }
        best
    }
}
