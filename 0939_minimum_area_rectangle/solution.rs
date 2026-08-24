// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

use std::collections::HashMap;

impl Solution {
    pub fn min_area_rect(points: Vec<Vec<i32>>) -> i32 {
        let mut by_x: HashMap<i32, Vec<i32>> = HashMap::new();
        for p in &points {
            by_x.entry(p[0]).or_default().push(p[1]);
        }
        let mut xs: Vec<i32> = by_x.keys().copied().collect();
        xs.sort_unstable();
        let mut last: HashMap<(i32, i32), i32> = HashMap::new();
        let mut ans = i64::MAX;
        for x in xs {
            let mut ys = by_x.remove(&x).unwrap();
            ys.sort_unstable();
            for i in 0..ys.len() {
                for j in (i + 1)..ys.len() {
                    let key = (ys[i], ys[j]);
                    if let Some(&prev) = last.get(&key) {
                        ans = ans.min((x - prev).abs() as i64 * (ys[j] - ys[i]) as i64);
                    }
                    last.insert(key, x);
                }
            }
        }
        if ans == i64::MAX { 0 } else { ans as i32 }
    }
}
