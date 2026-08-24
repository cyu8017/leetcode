// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

use std::collections::HashMap;

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut cnt1: HashMap<u64, HashMap<u64, i32>> = HashMap::new();
        let mut cnt2: HashMap<i32, HashMap<u64, i32>> = HashMap::new();
        for i in 0..n {
            let x1 = points[i][0];
            let y1 = points[i][1];
            for j in 0..i {
                let x2 = points[j][0];
                let y2 = points[j][1];
                let dx = x2 - x1;
                let dy = y2 - y1;
                let (k, b) = if dx == 0 {
                    (1e9_f64, x1 as f64)
                } else {
                    let k = dy as f64 / dx as f64;
                    let b = (y1 as i64 * dx as i64 - x1 as i64 * dy as i64) as f64 / dx as f64;
                    (k, b)
                };
                *cnt1.entry(k.to_bits()).or_default().entry(b.to_bits()).or_insert(0) += 1;
                let p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000);
                *cnt2.entry(p).or_default().entry(k.to_bits()).or_insert(0) += 1;
            }
        }
        let mut ans = 0;
        for e in cnt1.values() {
            let mut s = 0;
            for &t in e.values() {
                ans += s * t;
                s += t;
            }
        }
        for e in cnt2.values() {
            let mut s = 0;
            for &t in e.values() {
                ans -= s * t;
                s += t;
            }
        }
        ans
    }
}
