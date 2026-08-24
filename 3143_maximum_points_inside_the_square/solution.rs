// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

use std::collections::BTreeMap;

impl Solution {
    pub fn max_points_inside_square(points: Vec<Vec<i32>>, s: String) -> i32 {
        let sb = s.as_bytes();
        let mut g: BTreeMap<i32, Vec<usize>> = BTreeMap::new();
        for i in 0..points.len() {
            let key = points[i][0].abs().max(points[i][1].abs());
            g.entry(key).or_default().push(i);
        }
        let mut vis = [false; 26];
        let mut ans = 0;
        for idx in g.values() {
            for &i in idx {
                let j = (sb[i] - b'a') as usize;
                if vis[j] {
                    return ans;
                }
                vis[j] = true;
            }
            ans += idx.len() as i32;
        }
        ans
    }
}
