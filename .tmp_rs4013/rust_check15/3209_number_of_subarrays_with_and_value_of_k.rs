struct Solution;
// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mut pre: HashMap<i32, i64> = HashMap::new();
        let mut ans = 0i64;
        for x in nums {
            let mut cur: HashMap<i32, i64> = HashMap::new();
            for (&y, &v) in &pre {
                *cur.entry(x & y).or_insert(0) += v;
            }
            *cur.entry(x).or_insert(0) += 1;
            ans += *cur.get(&k).unwrap_or(&0);
            pre = cur;
        }
        ans
    }
}

fn main() {}
