// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

use std::collections::HashSet;

impl Solution {
    pub fn minimize_the_difference(mat: Vec<Vec<i32>>, target: i32) -> i32 {
        let mut possible: HashSet<i32> = HashSet::from([0]);
        for row in &mat {
            let uniq: HashSet<i32> = row.iter().copied().collect();
            let mut nxt: HashSet<i32> = HashSet::new();
            for &s in &possible {
                for &x in &uniq {
                    nxt.insert(s + x);
                }
            }
            let mut kept: HashSet<i32> = nxt.iter().copied().filter(|&v| v <= target).collect();
            let above: Vec<i32> = nxt.iter().copied().filter(|&v| v > target).collect();
            if let Some(&m) = above.iter().min() {
                kept.insert(m);
            }
            possible = if !kept.is_empty() {
                kept
            } else {
                HashSet::from([*nxt.iter().min().unwrap()])
            };
        }
        possible.iter().map(|&v| (v - target).abs()).min().unwrap()
    }
}
