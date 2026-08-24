// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        let mut cur = 0;
        let mut l = 0;
        for r in 0..nums.len() {
            let e = cnt.entry(nums[r]).or_insert(0);
            *e += 1;
            if *e == 2 {
                cur += 1;
            }
            while cur > k {
                let e = cnt.entry(nums[l]).or_insert(0);
                *e -= 1;
                if *e == 1 {
                    cur -= 1;
                }
                l += 1;
            }
            ans = ans.max(r - l + 1);
        }
        ans as i32
    }
}
