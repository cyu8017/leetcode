// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn grid_illumination(n: i32, lamps: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let _ = n;
        let mut rows: HashMap<i32, i32> = HashMap::new();
        let mut cols: HashMap<i32, i32> = HashMap::new();
        let mut diag1: HashMap<i32, i32> = HashMap::new();
        let mut diag2: HashMap<i32, i32> = HashMap::new();
        let mut lit: HashSet<(i32, i32)> = HashSet::new();
        for lamp in lamps {
            let (r, c) = (lamp[0], lamp[1]);
            if !lit.insert((r, c)) {
                continue;
            }
            *rows.entry(r).or_insert(0) += 1;
            *cols.entry(c).or_insert(0) += 1;
            *diag1.entry(r - c).or_insert(0) += 1;
            *diag2.entry(r + c).or_insert(0) += 1;
        }
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let (r, c) = (q[0], q[1]);
            let on = rows.get(&r).copied().unwrap_or(0) > 0
                || cols.get(&c).copied().unwrap_or(0) > 0
                || diag1.get(&(r - c)).copied().unwrap_or(0) > 0
                || diag2.get(&(r + c)).copied().unwrap_or(0) > 0;
            ans.push(if on { 1 } else { 0 });
            for i in r - 1..=r + 1 {
                for j in c - 1..=c + 1 {
                    if lit.remove(&(i, j)) {
                        *rows.get_mut(&i).unwrap() -= 1;
                        *cols.get_mut(&j).unwrap() -= 1;
                        *diag1.get_mut(&(i - j)).unwrap() -= 1;
                        *diag2.get_mut(&(i + j)).unwrap() -= 1;
                    }
                }
            }
        }
        ans
    }
}
