// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

use std::collections::HashMap;

impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            a = a.abs();
            b = b.abs();
            while b != 0 {
                (a, b) = (b, a % b);
            }
            a
        }

        let mut best = 0;
        for i in 0..points.len() {
            let mut slopes = HashMap::new();
            let mut local = 1;
            for j in i + 1..points.len() {
                let mut dx = points[j][0] - points[i][0];
                let mut dy = points[j][1] - points[i][1];
                let divisor = gcd(dx, dy);
                dx /= divisor;
                dy /= divisor;
                if dx < 0 || (dx == 0 && dy < 0) {
                    dx = -dx;
                    dy = -dy;
                }
                let count = slopes.entry((dx, dy)).or_insert(0);
                *count += 1;
                local = local.max(*count + 1);
            }
            best = best.max(local);
        }
        best
    }
}