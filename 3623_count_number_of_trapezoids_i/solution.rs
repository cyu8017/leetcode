// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

use std::collections::HashMap;

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for p in points {
            *cnt.entry(p[1]).or_insert(0) += 1;
        }
        let mut ans = 0i64;
        let mut s = 0i64;
        for &v in cnt.values() {
            let t = v as i64 * (v as i64 - 1) / 2;
            ans = (ans + s * t) % MOD;
            s += t;
        }
        ans as i32
    }
}
