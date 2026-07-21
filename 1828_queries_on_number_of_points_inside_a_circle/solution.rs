// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

impl Solution {
    pub fn count_points(points: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = Vec::with_capacity(queries.len());
        for query in &queries {
            let xq = query[0];
            let yq = query[1];
            let r = query[2];
            let radius_sq = r * r;
            let mut count = 0;
            for point in &points {
                let dx = point[0] - xq;
                let dy = point[1] - yq;
                if dx * dx + dy * dy <= radius_sq {
                    count += 1;
                }
            }
            result.push(count);
        }
        result
    }
}
