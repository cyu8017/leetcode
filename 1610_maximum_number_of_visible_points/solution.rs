// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

impl Solution {
    pub fn visible_points(points: Vec<Vec<i32>>, angle: i32, location: Vec<i32>) -> i32 {
        let mut same = 0;
        let mut a = Vec::new();
        for p in &points {
            let dx = (p[0] - location[0]) as f64;
            let dy = (p[1] - location[1]) as f64;
            if dx == 0.0 && dy == 0.0 {
                same += 1;
            } else {
                a.push(dy.atan2(dx));
            }
        }
        a.sort_by(|x, y| x.partial_cmp(y).unwrap());
        let n = a.len();
        let mut ext = a.clone();
        for &x in &a {
            ext.push(x + 2.0 * std::f64::consts::PI);
        }
        let width = angle as f64 * std::f64::consts::PI / 180.0 + 1e-12;
        let mut left = 0usize;
        let mut best = 0usize;
        for right in 0..ext.len() {
            while ext[right] - ext[left] > width {
                left += 1;
            }
            let mut cur = right - left + 1;
            if cur > n {
                cur = n;
            }
            best = best.max(cur);
        }
        (best + same) as i32
    }
}
