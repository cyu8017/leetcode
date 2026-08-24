// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

use std::collections::HashMap;

impl Solution {
    pub fn max_total(value: Vec<i32>, limit: Vec<i32>) -> i64 {
        let mut g: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..value.len() {
            g.entry(limit[i]).or_default().push(value[i]);
        }
        let mut ans = 0i64;
        for (lim, mut vs) in g {
            vs.sort_unstable_by(|a, b| b.cmp(a));
            for i in 0..vs.len().min(lim as usize) {
                ans += vs[i] as i64;
            }
        }
        ans
    }
}
