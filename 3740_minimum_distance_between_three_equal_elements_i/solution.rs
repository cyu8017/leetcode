// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_distance(nums: Vec<i32>) -> i32 {
        let mut g: HashMap<i32, Vec<i32>> = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            g.entry(x).or_default().push(i as i32);
        }
        const INF: i32 = 1 << 30;
        let mut ans = INF;
        for ls in g.values() {
            let m = ls.len();
            for h in 0..m.saturating_sub(2) {
                ans = ans.min((ls[h + 2] - ls[h]) * 2);
            }
        }
        if ans == INF { -1 } else { ans }
    }
}
