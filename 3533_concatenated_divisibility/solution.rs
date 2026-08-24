// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

use std::collections::HashMap;

impl Solution {
    pub fn concatenated_divisibility(mut nums: Vec<i32>, k: i32) -> Vec<i32> {
        nums.sort();
        let n = nums.len();
        let mut pows = vec![0; n];
        for i in 0..n {
            let mut p = 1;
            let num = nums[i];
            if num == 0 {
                p = 10 % k;
            } else {
                let mut x = num;
                while x > 0 {
                    p = p * 10 % k;
                    x /= 10;
                }
            }
            pows[i] = p;
        }
        fn dp(mask: i32, md: i32, n: usize, k: i32, nums: &[i32], pows: &[i32], memo: &mut HashMap<(i32, i32), bool>) -> bool {
            if mask == (1 << n) - 1 {
                return md == 0;
            }
            let key = (mask, md);
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            for i in 0..n {
                if (mask >> i) & 1 == 0 {
                    let nm = (md * pows[i] + nums[i]) % k;
                    if dp(mask | (1 << i), nm, n, k, nums, pows, memo) {
                        memo.insert(key, true);
                        return true;
                    }
                }
            }
            memo.insert(key, false);
            false
        }
        fn reconstruct(mask: i32, md: i32, n: usize, k: i32, nums: &[i32], pows: &[i32], memo: &mut HashMap<(i32, i32), bool>) -> Vec<i32> {
            for i in 0..n {
                if (mask >> i) & 1 == 0 {
                    let nm = (md * pows[i] + nums[i]) % k;
                    if dp(mask | (1 << i), nm, n, k, nums, pows, memo) {
                        let mut rest = reconstruct(mask | (1 << i), nm, n, k, nums, pows, memo);
                        rest.insert(0, nums[i]);
                        return rest;
                    }
                }
            }
            vec![]
        }
        let mut memo = HashMap::new();
        if !dp(0, 0, n, k, &nums, &pows, &mut memo) {
            return vec![];
        }
        reconstruct(0, 0, n, k, &nums, &pows, &mut memo)
    }
}
