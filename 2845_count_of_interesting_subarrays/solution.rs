// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn count_interesting_subarrays(nums: Vec<i32>, modulo: i32, k: i32) -> i64 {
        let mut freq: HashMap<i32, i64> = HashMap::new();
        freq.insert(0, 1);
        let mut ans = 0i64;
        let mut pref = 0i32;
        for v in nums {
            if v % modulo == k {
                pref += 1;
            }
            let mut need = (pref - k) % modulo;
            if need < 0 {
                need += modulo;
            }
            ans += *freq.get(&need).unwrap_or(&0);
            *freq.entry(pref % modulo).or_insert(0) += 1;
        }
        ans
    }
}
