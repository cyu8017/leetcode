// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

impl Solution {
    pub fn best_coordinate(towers: Vec<Vec<i32>>, radius: i32) -> Vec<i32> {
        let mut best = vec![0, 0];
        let mut quality = -1;
        for x in 0..=50 {
            for y in 0..=50 {
                let mut q = 0;
                for t in &towers {
                    let d = (((x - t[0]) as f64).hypot((y - t[1]) as f64));
                    if d <= radius as f64 {
                        q += (t[2] as f64 / (1.0 + d)) as i32;
                    }
                }
                if q > quality {
                    quality = q;
                    best = vec![x, y];
                }
            }
        }
        best
    }
}
