// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

use std::collections::BTreeMap;

impl Solution {
    pub fn minimum_distance(points: Vec<Vec<i32>>) -> i32 {
        let mut st1: BTreeMap<i32, i32> = BTreeMap::new();
        let mut st2: BTreeMap<i32, i32> = BTreeMap::new();
        let merge = |st: &mut BTreeMap<i32, i32>, x: i32, v: i32| {
            let e = st.entry(x).or_insert(0);
            *e += v;
            if *e == 0 {
                st.remove(&x);
            }
        };
        for p in &points {
            merge(&mut st1, p[0] + p[1], 1);
            merge(&mut st2, p[0] - p[1], 1);
        }
        let mut ans = i32::MAX;
        for p in &points {
            let (x, y) = (p[0], p[1]);
            merge(&mut st1, x + y, -1);
            merge(&mut st2, x - y, -1);
            let d1 = st1.keys().next_back().copied().unwrap() - st1.keys().next().copied().unwrap();
            let d2 = st2.keys().next_back().copied().unwrap() - st2.keys().next().copied().unwrap();
            ans = ans.min(d1.max(d2));
            merge(&mut st1, x + y, 1);
            merge(&mut st2, x - y, 1);
        }
        ans
    }
}
