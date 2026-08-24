// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

use std::collections::HashSet;

impl Solution {
    pub fn count_distinct_integers(nums: Vec<i32>) -> i32 {
        fn rev(mut x: i32) -> i32 {
            let mut r = 0;
            while x > 0 {
                r = r * 10 + x % 10;
                x /= 10;
            }
            r
        }
        let mut seen = HashSet::new();
        for x in nums {
            seen.insert(x);
            seen.insert(rev(x));
        }
        seen.len() as i32
    }
}
