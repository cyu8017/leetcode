struct Solution;

// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

use std::collections::HashSet;

impl Solution {
    pub fn max_count(banned: Vec<i32>, n: i32, max_sum: i32) -> i32 {
        let ban: HashSet<i32> = banned.into_iter().collect();
        let mut ans = 0;
        let mut sum = 0;
        for i in 1..=n {
            if ban.contains(&i) {
                continue;
            }
            if sum + i > max_sum {
                break;
            }
            sum += i;
            ans += 1;
        }
        ans
    }
}

fn main() {}
