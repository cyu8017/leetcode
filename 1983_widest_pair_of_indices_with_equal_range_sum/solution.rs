// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

use std::collections::HashMap;

impl Solution {
    pub fn widest_pair_of_indices(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut first: HashMap<i32, i32> = HashMap::from([(0, -1)]);
        let mut ans = 0;
        let mut s = 0;
        for (i, (&a, &b)) in nums1.iter().zip(nums2.iter()).enumerate() {
            s += a - b;
            if let Some(&j) = first.get(&s) {
                ans = ans.max(i as i32 - j);
            } else {
                first.insert(s, i as i32);
            }
        }
        ans
    }
}
