// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(s: String, cost: Vec<i32>) -> i64 {
        let mut tot = 0i64;
        let mut g: HashMap<u8, i64> = HashMap::new();
        let bytes = s.as_bytes();
        for i in 0..cost.len() {
            tot += cost[i] as i64;
            *g.entry(bytes[i]).or_insert(0) += cost[i] as i64;
        }
        let mut ans = tot;
        for &x in g.values() {
            ans = ans.min(tot - x);
        }
        ans
    }
}
