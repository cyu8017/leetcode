// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i32 {
        fn digit_sum(mut x: i32) -> i32 {
            let mut s = 0;
            while x > 0 {
                s += x % 10;
                x /= 10;
            }
            s
        }
        let mut best = HashMap::new();
        let mut ans = -1;
        for x in nums {
            let ds = digit_sum(x);
            if let Some(&prev) = best.get(&ds) {
                ans = ans.max(prev + x);
                if x > prev {
                    best.insert(ds, x);
                }
            } else {
                best.insert(ds, x);
            }
        }
        ans
    }
}
