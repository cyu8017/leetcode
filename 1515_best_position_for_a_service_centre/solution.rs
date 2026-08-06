// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

impl Solution {
    pub fn get_min_dist_sum(positions: Vec<Vec<i32>>) -> f64 {
        let n = positions.len() as f64;
        let mut x: f64 = positions.iter().map(|p| p[0] as f64).sum::<f64>() / n;
        let mut y: f64 = positions.iter().map(|p| p[1] as f64).sum::<f64>() / n;
        let distance = |a: f64, b: f64| -> f64 {
            positions
                .iter()
                .map(|p| ((a - p[0] as f64).hypot(b - p[1] as f64)))
                .sum()
        };
        for _ in 0..10000 {
            let mut num_x = 0.0;
            let mut num_y = 0.0;
            let mut den = 0.0;
            let mut coincident = None;
            for p in &positions {
                let d = (x - p[0] as f64).hypot(y - p[1] as f64);
                if d < 1e-12 {
                    coincident = Some((p[0] as f64, p[1] as f64));
                    break;
                }
                num_x += p[0] as f64 / d;
                num_y += p[1] as f64 / d;
                den += 1.0 / d;
            }
            let (nx, ny) = if let Some(c) = coincident {
                c
            } else {
                (num_x / den, num_y / den)
            };
            if (nx - x).hypot(ny - y) < 1e-8 {
                x = nx;
                y = ny;
                break;
            }
            x = nx;
            y = ny;
        }
        distance(x, y)
    }
}
