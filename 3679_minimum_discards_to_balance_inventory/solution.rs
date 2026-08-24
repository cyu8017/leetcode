// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

use std::collections::HashMap;

impl Solution {
    pub fn min_arrivals_to_discard(arrivals: Vec<i32>, w: i32, m: i32) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let n = arrivals.len();
        let w = w as usize;
        let mut marked = vec![0i32; n];
        let mut ans = 0;
        for i in 0..n {
            let x = arrivals[i];
            if i >= w {
                *cnt.entry(arrivals[i - w]).or_insert(0) -= marked[i - w];
            }
            if *cnt.get(&x).unwrap_or(&0) >= m {
                ans += 1;
            } else {
                marked[i] = 1;
                *cnt.entry(x).or_insert(0) += 1;
            }
        }
        ans
    }
}
