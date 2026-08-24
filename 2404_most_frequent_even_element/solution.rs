// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

use std::collections::HashMap;

impl Solution {
    pub fn most_frequent_even(nums: Vec<i32>) -> i32 {
        let mut cnt = HashMap::new();
        let mut ans = -1;
        let mut best = 0;
        for x in nums {
            if x % 2 != 0 {
                continue;
            }
            let c = cnt.entry(x).or_insert(0);
            *c += 1;
            if *c > best || (*c == best && (ans == -1 || x < ans)) {
                best = *c;
                ans = x;
            }
        }
        ans
    }
}
