// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

use std::collections::HashMap;

impl Solution {
    pub fn min_area_free_rect(points: Vec<Vec<i32>>) -> f64 {
        let n = points.len();
        let mut groups: HashMap<((i64, i64), i64), Vec<(usize, usize)>> = HashMap::new();
        for i in 0..n {
            for j in (i + 1)..n {
                let cx = points[i][0] as i64 + points[j][0] as i64;
                let cy = points[i][1] as i64 + points[j][1] as i64;
                let dx = points[i][0] as i64 - points[j][0] as i64;
                let dy = points[i][1] as i64 - points[j][1] as i64;
                let dist = dx * dx + dy * dy;
                groups.entry(((cx, cy), dist)).or_default().push((i, j));
            }
        }
        let mut ans = 1e300;
        for pairs in groups.values() {
            for a in 0..pairs.len() {
                for b in (a + 1)..pairs.len() {
                    let p1 = pairs[a].0;
                    let p2 = pairs[b].0;
                    let q2 = pairs[b].1;
                    let d1 = ((points[p1][0] - points[p2][0]) as f64).hypot((points[p1][1] - points[p2][1]) as f64);
                    let d2 = ((points[p1][0] - points[q2][0]) as f64).hypot((points[p1][1] - points[q2][1]) as f64);
                    let area = d1 * d2;
                    if area > 0.0 {
                        ans = ans.min(area);
                    }
                }
            }
        }
        if ans >= 1e299 { 0.0 } else { ans }
    }
}
