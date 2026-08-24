struct Solution;
// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let mut pos = 0;
        for (i, &x) in nums.iter().enumerate() {
            if x == k {
                pos = i;
                break;
            }
        }
        let mut bal: HashMap<i32, i32> = HashMap::new();
        bal.insert(0, 1);
        let mut cur = 0;
        for i in (0..pos).rev() {
            cur += if nums[i] < k { -1 } else { 1 };
            *bal.entry(cur).or_insert(0) += 1;
        }
        let mut ans = *bal.get(&0).unwrap_or(&0) + *bal.get(&1).unwrap_or(&0);
        cur = 0;
        for i in pos + 1..nums.len() {
            cur += if nums[i] < k { -1 } else { 1 };
            ans += *bal.get(&(-cur)).unwrap_or(&0) + *bal.get(&(1 - cur)).unwrap_or(&0);
        }
        ans
    }
}

fn main() {}
