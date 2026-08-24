// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

use std::collections::HashMap;

impl Solution {
    pub fn max_activated(points: Vec<Vec<i32>>) -> i32 {
        const M: i64 = 3_000_000_000;
        let mut p = HashMap::new();
        let mut size = HashMap::new();
        fn find(x: i64, p: &mut HashMap<i64, i64>, size: &mut HashMap<i64, i32>) -> i64 {
            if !p.contains_key(&x) {
                p.insert(x, x);
                size.insert(x, 1);
            }
            let px = p[&x];
            if px != x {
                let r = find(px, p, size);
                p.insert(x, r);
                return r;
            }
            x
        }
        fn unite(a: i64, b: i64, p: &mut HashMap<i64, i64>, size: &mut HashMap<i64, i32>) {
            let pa = find(a, p, size);
            let pb = find(b, p, size);
            if pa == pb {
                return;
            }
            if size[&pa] > size[&pb] {
                p.insert(pb, pa);
                let add = size[&pb];
                *size.get_mut(&pa).unwrap() += add;
            } else {
                p.insert(pa, pb);
                let add = size[&pa];
                *size.get_mut(&pb).unwrap() += add;
            }
        }
        for pt in &points {
            unite(pt[0] as i64, pt[1] as i64 + M, &mut p, &mut size);
        }
        let mut cnt = HashMap::new();
        for pt in &points {
            let r = find(pt[0] as i64, &mut p, &mut size);
            *cnt.entry(r).or_insert(0) += 1;
        }
        let mut mx1 = 0;
        let mut mx2 = 0;
        for &x in cnt.values() {
            if mx1 < x {
                mx2 = mx1;
                mx1 = x;
            } else if mx2 < x {
                mx2 = x;
            }
        }
        mx1 + mx2 + 1
    }
}
