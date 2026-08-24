// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

use std::collections::HashMap;

impl Solution {
    pub fn subarray_majority(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = vec![0; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let thresh = q[2];
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for i in l..=r {
                *freq.entry(nums[i]).or_insert(0) += 1;
            }
            let mut best_val = -1;
            let mut best_cnt = 0;
            for (&v, &c) in &freq {
                if c >= thresh && (c > best_cnt || (c == best_cnt && (best_val == -1 || v < best_val))) {
                    best_cnt = c;
                    best_val = v;
                }
            }
            ans[qi] = best_val;
        }
        ans
    }
}
