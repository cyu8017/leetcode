// LeetCode 3868 - Minimum Cost to Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut cnt2 = HashMap::new();
        for x in nums2 {
            *cnt2.entry(x).or_insert(0) += 1;
        }
        let mut cnt1 = HashMap::new();
        for x in nums1 {
            if let Some(v) = cnt2.get_mut(&x) {
                if *v > 0 {
                    *v -= 1;
                    continue;
                }
            }
            *cnt1.entry(x).or_insert(0) += 1;
        }
        let mut ans = 0;
        for &v in cnt1.values() {
            if v % 2 == 1 {
                return -1;
            }
            ans += v / 2;
        }
        for &v in cnt2.values() {
            if v % 2 == 1 {
                return -1;
            }
        }
        ans
    }
}
