// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut c: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        for x in nums {
            let need = k - x;
            if let Some(cnt) = c.get_mut(&need) {
                if *cnt > 0 {
                    *cnt -= 1;
                    ans += 1;
                    continue;
                }
            }
            *c.entry(x).or_insert(0) += 1;
        }
        ans
    }
}
