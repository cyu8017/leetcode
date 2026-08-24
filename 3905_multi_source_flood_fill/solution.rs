// LeetCode 3905 - Multi-Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

use std::collections::BTreeMap;

impl Solution {
    pub fn color_grid(n: i32, m: i32, sources: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let m = m as usize;
        let mut ans = vec![vec![0; m]; n];
        let mut q = sources;
        let dirs = [-1, 0, 1, 0, -1];
        for s in &q {
            ans[s[0] as usize][s[1] as usize] = s[2];
        }
        while !q.is_empty() {
            let mut vis = BTreeMap::new();
            for curr in &q {
                let r = curr[0];
                let c = curr[1];
                let color = curr[2];
                for i in 0..4 {
                    let x = r + dirs[i];
                    let y = c + dirs[i + 1];
                    if x >= 0 && x < n as i32 && y >= 0 && y < m as i32 && ans[x as usize][y as usize] == 0 {
                        let key = (x, y);
                        let e = vis.entry(key).or_insert(0);
                        if color > *e {
                            *e = color;
                        }
                    }
                }
            }
            q.clear();
            for ((x, y), color) in vis {
                ans[x as usize][y as usize] = color;
                q.push(vec![x, y, color]);
            }
        }
        ans
    }
}
