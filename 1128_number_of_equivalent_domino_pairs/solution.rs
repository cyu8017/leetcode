// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let mut count = HashMap::new();
        let mut ans = 0;
        for d in dominoes {
            let (a, b) = if d[0] > d[1] { (d[1], d[0]) } else { (d[0], d[1]) };
            let key = a * 10 + b;
            ans += *count.get(&key).unwrap_or(&0);
            *count.entry(key).or_insert(0) += 1;
        }
        ans
    }
}
