// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let mut vals: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, row) in grid.iter().enumerate() {
            let mut seen = HashSet::new();
            for &v in row {
                if seen.insert(v) {
                    vals.entry(v).or_default().push(i);
                }
            }
        }
        let mut arr: Vec<i32> = vals.keys().copied().collect();
        arr.sort_unstable_by(|a, b| b.cmp(a));
        let nmask = 1 << m;
        let mut dp = vec![0; nmask];
        for v in arr {
            let mut ndp = dp.clone();
            for &r in &vals[&v] {
                let bit = 1 << r;
                for mask in 0..nmask {
                    if mask & bit != 0 {
                        continue;
                    }
                    let cand = dp[mask] + v;
                    let nm = mask | bit;
                    if cand > ndp[nm] {
                        ndp[nm] = cand;
                    }
                }
            }
            dp = ndp;
        }
        *dp.iter().max().unwrap()
    }
}
