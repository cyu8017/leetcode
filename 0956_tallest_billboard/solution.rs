// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

use std::collections::HashMap;

impl Solution {
    pub fn tallest_billboard(rods: Vec<i32>) -> i32 {
        let mut dp = HashMap::new();
        dp.insert(0, 0);
        for rod in rods {
            let cur = dp.clone();
            for (&diff, &taller) in &cur {
                let e = dp.entry(diff + rod).or_insert(0);
                *e = (*e).max(taller + rod);
                let nd = (diff - rod).abs();
                let nt = if diff >= rod { taller } else { taller - diff + rod };
                let e = dp.entry(nd).or_insert(0);
                *e = (*e).max(nt);
            }
        }
        *dp.get(&0).unwrap_or(&0)
    }
}
