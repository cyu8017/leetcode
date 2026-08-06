// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

use std::collections::HashMap;

impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let target = nums.iter().map(|&x| x as i64).sum::<i64>() % p as i64;
        if target == 0 {
            return 0;
        }
        let mut seen = HashMap::new();
        seen.insert(0i64, -1i32);
        let mut prefix = 0i64;
        let mut answer = nums.len() as i32;
        for (i, &x) in nums.iter().enumerate() {
            prefix = (prefix + x as i64) % p as i64;
            let need = (prefix - target + p as i64) % p as i64;
            if let Some(&idx) = seen.get(&need) {
                answer = answer.min(i as i32 - idx);
            }
            seen.insert(prefix, i as i32);
        }
        if answer < nums.len() as i32 {
            answer
        } else {
            -1
        }
    }
}
