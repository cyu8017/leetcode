// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

use std::collections::BTreeMap;

impl Solution {
    pub fn split_painting(segments: Vec<Vec<i32>>) -> Vec<Vec<i64>> {
        let mut diff: BTreeMap<i32, i64> = BTreeMap::new();
        for seg in segments {
            let (s, e, c) = (seg[0], seg[1], seg[2] as i64);
            *diff.entry(s).or_insert(0) += c;
            *diff.entry(e).or_insert(0) -= c;
        }
        let points: Vec<i32> = diff.keys().copied().collect();
        let mut ans = Vec::new();
        let mut cur = 0i64;
        for i in 0..points.len() - 1 {
            cur += diff[&points[i]];
            if cur != 0 {
                ans.push(vec![points[i] as i64, points[i + 1] as i64, cur]);
            }
        }
        ans
    }
}
