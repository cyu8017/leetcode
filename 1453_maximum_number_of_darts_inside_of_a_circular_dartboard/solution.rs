// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

impl Solution {
    pub fn num_points(darts: Vec<Vec<i32>>, r: i32) -> i32 {
        let mut ans = if darts.is_empty() { 0 } else { 1 };
        let r2 = (r * r) as f64;
        for i in 0..darts.len() {
            for j in i + 1..darts.len() {
                let (x1, y1) = (darts[i][0] as f64, darts[i][1] as f64);
                let (x2, y2) = (darts[j][0] as f64, darts[j][1] as f64);
                let dx = x2 - x1;
                let dy = y2 - y1;
                let d2 = dx * dx + dy * dy;
                if d2 > 4.0 * r2 || d2 == 0.0 {
                    continue;
                }
                let d = d2.sqrt();
                let h = (r2 - d2 / 4.0).sqrt();
                let mx = (x1 + x2) / 2.0;
                let my = (y1 + y2) / 2.0;
                for sign in [-1.0, 1.0] {
                    let cx = mx + sign * (-dy) * h / d;
                    let cy = my + sign * dx * h / d;
                    let count = darts
                        .iter()
                        .filter(|p| {
                            let x = p[0] as f64;
                            let y = p[1] as f64;
                            (x - cx) * (x - cx) + (y - cy) * (y - cy) <= r2 + 1e-7
                        })
                        .count() as i32;
                    ans = ans.max(count);
                }
            }
        }
        ans
    }
}
