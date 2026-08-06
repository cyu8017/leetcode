// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

impl Solution {
    pub fn outer_trees(trees: Vec<Vec<i32>>) -> Vec<f64> {
        let mut pts: Vec<(f64, f64)> = trees
            .iter()
            .map(|p| (p[0] as f64, p[1] as f64))
            .collect();

        // Deterministic Fisher–Yates (no external RNG crate)
        let mut seed: u64 = 0x9e37_79b9_7f4a_7c15;
        for i in (1..pts.len()).rev() {
            seed = seed
                .wrapping_mul(6364136223846793005)
                .wrapping_add(1);
            let j = (seed as usize) % (i + 1);
            pts.swap(i, j);
        }

        fn dist(a: (f64, f64), b: (f64, f64)) -> f64 {
            let dx = a.0 - b.0;
            let dy = a.1 - b.1;
            (dx * dx + dy * dy).sqrt()
        }

        fn circle2(a: (f64, f64), b: (f64, f64)) -> ((f64, f64), f64) {
            let c = ((a.0 + b.0) / 2.0, (a.1 + b.1) / 2.0);
            (c, dist(a, b) / 2.0)
        }

        fn circle3(a: (f64, f64), b: (f64, f64), c: (f64, f64)) -> ((f64, f64), f64) {
            let (ax, ay) = a;
            let (bx, by) = b;
            let (cx, cy) = c;
            let d = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
            if d.abs() < 1e-12 {
                let candidates = [circle2(a, b), circle2(a, c), circle2(b, c)];
                return candidates
                    .into_iter()
                    .min_by(|x, y| x.1.partial_cmp(&y.1).unwrap())
                    .unwrap();
            }
            let ux = ((ax * ax + ay * ay) * (by - cy)
                + (bx * bx + by * by) * (cy - ay)
                + (cx * cx + cy * cy) * (ay - by))
                / d;
            let uy = ((ax * ax + ay * ay) * (cx - bx)
                + (bx * bx + by * by) * (ax - cx)
                + (cx * cx + cy * cy) * (bx - ax))
                / d;
            let center = (ux, uy);
            (center, dist(center, a))
        }

        fn inside(cir: Option<((f64, f64), f64)>, p: (f64, f64)) -> bool {
            match cir {
                None => false,
                Some((c, r)) => dist(c, p) <= r + 1e-9,
            }
        }

        let mut circle: Option<((f64, f64), f64)> = None;
        for i in 0..pts.len() {
            let p = pts[i];
            if !inside(circle, p) {
                circle = Some((p, 0.0));
                for j in 0..i {
                    let q = pts[j];
                    if !inside(circle, q) {
                        circle = Some(circle2(p, q));
                        for k in 0..j {
                            let r = pts[k];
                            if !inside(circle, r) {
                                circle = Some(circle3(p, q, r));
                            }
                        }
                    }
                }
            }
        }
        let ((x, y), r) = circle.unwrap();
        vec![x, y, r]
    }
}
