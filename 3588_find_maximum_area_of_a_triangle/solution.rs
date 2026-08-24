// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

use std::collections::HashMap;

impl Solution {
    pub fn max_area(mut coords: Vec<Vec<i32>>) -> i64 {
        let calc = |coords: &[Vec<i32>]| -> i64 {
            let mut mn = 1_000_000_000;
            let mut mx = 0;
            let mut f: HashMap<i32, i32> = HashMap::new();
            let mut g: HashMap<i32, i32> = HashMap::new();
            for c in coords {
                let (x, y) = (c[0], c[1]);
                mn = mn.min(x);
                mx = mx.max(x);
                if let Some(&fy) = f.get(&x) {
                    f.insert(x, fy.min(y));
                    g.insert(x, g[&x].max(y));
                } else {
                    f.insert(x, y);
                    g.insert(x, y);
                }
            }
            let mut ans = 0i64;
            for (&x, &y) in &f {
                let d = g[&x] - y;
                ans = ans.max(d as i64 * (mx - x).max(x - mn) as i64);
            }
            ans
        };
        let mut ans = calc(&coords);
        for c in &mut coords {
            c.swap(0, 1);
        }
        ans = ans.max(calc(&coords));
        if ans > 0 { ans } else { -1 }
    }
}
