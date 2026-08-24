// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

use std::collections::HashSet;

impl Solution {
    pub fn find_missing_elements(nums: Vec<i32>) -> Vec<i32> {
        let mut mn = 100;
        let mut mx = 0;
        let mut s = HashSet::new();
        for &x in &nums {
            mn = mn.min(x);
            mx = mx.max(x);
            s.insert(x);
        }
        let mut ans = Vec::new();
        for x in (mn + 1)..mx {
            if !s.contains(&x) {
                ans.push(x);
            }
        }
        ans
    }
}
