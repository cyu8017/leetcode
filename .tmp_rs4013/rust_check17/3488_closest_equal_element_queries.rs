struct Solution;
// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

use std::collections::HashMap;

impl Solution {
    pub fn solve_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            pos.entry(x).or_default().push(i);
        }
        let mut ans = vec![0; queries.len()];
        for (qi, &idx) in queries.iter().enumerate() {
            let idx = idx as usize;
            let x = nums[idx];
            let arr = &pos[&x];
            if arr.len() == 1 {
                ans[qi] = -1;
                continue;
            }
            let mut best = n as i32;
            for &p in arr {
                if p == idx {
                    continue;
                }
                let mut d = (p as i32 - idx as i32).abs();
                d = d.min(n as i32 - d);
                if d < best {
                    best = d;
                }
            }
            ans[qi] = best;
        }
        ans
    }
}

fn main() {}
