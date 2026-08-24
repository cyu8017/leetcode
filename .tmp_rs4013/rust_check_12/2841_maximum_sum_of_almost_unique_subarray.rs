struct Solution;
// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn max_sum(nums: Vec<i32>, m: i32, k: i32) -> i64 {
        let k = k as usize;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut sum = 0i64;
        let mut ans = 0i64;
        for i in 0..nums.len() {
            *freq.entry(nums[i]).or_insert(0) += 1;
            sum += nums[i] as i64;
            if i >= k {
                let out = nums[i - k];
                sum -= out as i64;
                if let Some(c) = freq.get_mut(&out) {
                    *c -= 1;
                    if *c == 0 {
                        freq.remove(&out);
                    }
                }
            }
            if i + 1 >= k && freq.len() as i32 >= m {
                ans = ans.max(sum);
            }
        }
        ans
    }
}

fn main() {}
