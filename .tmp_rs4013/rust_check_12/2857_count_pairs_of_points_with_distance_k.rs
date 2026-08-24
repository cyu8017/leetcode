struct Solution;
// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_pairs(coordinates: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut freq: HashMap<(i32, i32), i32> = HashMap::new();
        let mut ans = 0i32;
        for p in coordinates {
            let x = p[0];
            let y = p[1];
            for a in 0..=k {
                let b = k - a;
                ans += *freq.get(&(x ^ a, y ^ b)).unwrap_or(&0);
            }
            *freq.entry((x, y)).or_insert(0) += 1;
        }
        ans
    }
}

fn main() {}
