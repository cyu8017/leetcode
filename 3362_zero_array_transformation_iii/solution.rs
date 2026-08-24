// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

use std::collections::BinaryHeap;

impl Solution {
    pub fn max_removal(nums: Vec<i32>, mut queries: Vec<Vec<i32>>) -> i32 {
        queries.sort_unstable_by(|a, b| a[0].cmp(&b[0]));
        let mut h = BinaryHeap::new();
        let n = nums.len();
        let mut diff = vec![0i32; n + 1];
        let mut j = 0;
        let mut used = 0;
        let mut cur = 0;
        for i in 0..n {
            cur += diff[i];
            while j < queries.len() && queries[j][0] == i as i32 {
                h.push(queries[j][1]);
                j += 1;
            }
            while cur < nums[i] {
                if h.is_empty() || *h.peek().unwrap() < i as i32 {
                    return -1;
                }
                let r = h.pop().unwrap();
                cur += 1;
                diff[r as usize + 1] -= 1;
                used += 1;
            }
        }
        queries.len() as i32 - used
    }
}
