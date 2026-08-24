// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

use std::collections::HashSet;

impl Solution {
    pub fn powerful_integers(x: i32, y: i32, bound: i32) -> Vec<i32> {
        let mut ans = HashSet::new();
        let mut a = 1i64;
        while a < bound as i64 {
            let mut b = 1i64;
            while a + b <= bound as i64 {
                ans.insert((a + b) as i32);
                if y == 1 {
                    break;
                }
                b *= y as i64;
            }
            if x == 1 {
                break;
            }
            a *= x as i64;
        }
        ans.into_iter().collect()
    }
}
