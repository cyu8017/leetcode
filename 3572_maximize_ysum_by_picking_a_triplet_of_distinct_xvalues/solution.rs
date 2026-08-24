// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

use std::collections::HashSet;

impl Solution {
    pub fn max_sum_distinct_triplet(x: Vec<i32>, y: Vec<i32>) -> i32 {
        let n = x.len();
        let mut arr: Vec<(i32, i32)> = (0..n).map(|i| (x[i], y[i])).collect();
        arr.sort_by(|a, b| b.1.cmp(&a.1));
        let mut ans = 0;
        let mut vis = HashSet::new();
        for (a, b) in arr {
            if vis.insert(a) {
                ans += b;
                if vis.len() == 3 {
                    return ans;
                }
            }
        }
        -1
    }
}
