// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        let mut best = 0.0;
        let n = points.len();
        for i in 0..n {
            let (x1, y1) = (points[i][0], points[i][1]);
            for j in i + 1..n {
                let (x2, y2) = (points[j][0], points[j][1]);
                for k in j + 1..n {
                    let (x3, y3) = (points[k][0], points[k][1]);
                    let area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)).abs() as f64 / 2.0;
                    best = best.max(area);
                }
            }
        }
        best
    }
}
