// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

use std::collections::HashMap;

impl Solution {
    pub fn interchangeable_rectangles(rectangles: Vec<Vec<i32>>) -> i64 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut freq = HashMap::new();
        let mut ans = 0i64;
        for rect in rectangles {
            let g = gcd(rect[0], rect[1]);
            let key = (rect[0] / g, rect[1] / g);
            ans += *freq.get(&key).unwrap_or(&0);
            *freq.entry(key).or_insert(0) += 1;
        }
        ans
    }
}
