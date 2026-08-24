struct Solution;
// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let ok_area = |y: f64| -> f64 {
            let mut below = 0.0;
            for sq in &squares {
                let yi = sq[1] as f64;
                let l = sq[2] as f64;
                let top = yi + l;
                if y <= yi {
                    continue;
                }
                if y >= top {
                    below += l * l;
                } else {
                    below += l * (y - yi);
                }
            }
            below
        };
        let mut total = 0.0;
        for sq in &squares {
            let l = sq[2] as f64;
            total += l * l;
        }
        let mut lo = 0.0;
        let mut hi = 2e9;
        for _ in 0..60 {
            let mid = (lo + hi) / 2.0;
            if ok_area(mid) * 2.0 < total {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        hi
    }
}

fn main() {}
