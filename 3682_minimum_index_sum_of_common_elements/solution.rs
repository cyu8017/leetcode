// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        const INF: i32 = 1 << 30;
        let mut d = HashMap::new();
        for (i, &x) in nums2.iter().enumerate() {
            d.entry(x).or_insert(i as i32);
        }
        let mut ans = INF;
        for (i, &x) in nums1.iter().enumerate() {
            if let Some(&j) = d.get(&x) {
                ans = ans.min(i as i32 + j);
            }
        }
        if ans == INF {
            -1
        } else {
            ans
        }
    }
}
