struct Solution;

// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(basket1: Vec<i32>, basket2: Vec<i32>) -> i64 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut mn = i32::MAX;
        for x in basket1 {
            *freq.entry(x).or_insert(0) += 1;
            mn = mn.min(x);
        }
        for x in basket2 {
            *freq.entry(x).or_insert(0) -= 1;
            mn = mn.min(x);
        }
        let mut extra = Vec::new();
        for (&v, &c) in &freq {
            if c % 2 != 0 {
                return -1;
            }
            for _ in 0..c.abs() / 2 {
                extra.push(v);
            }
        }
        extra.sort_unstable();
        let mut ans = 0i64;
        for i in 0..extra.len() / 2 {
            let a = extra[i] as i64;
            let b = 2 * mn as i64;
            ans += a.min(b);
        }
        ans
    }
}

fn main() {}
