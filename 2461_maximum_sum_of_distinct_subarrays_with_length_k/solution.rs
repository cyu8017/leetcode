// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut sum = 0i64;
        let mut ans = 0i64;
        for i in 0..nums.len() {
            sum += nums[i] as i64;
            *cnt.entry(nums[i]).or_insert(0) += 1;
            if i >= k {
                sum -= nums[i - k] as i64;
                let e = cnt.get_mut(&nums[i - k]).unwrap();
                *e -= 1;
                if *e == 0 {
                    cnt.remove(&nums[i - k]);
                }
            }
            if i + 1 >= k && cnt.len() == k {
                ans = ans.max(sum);
            }
        }
        ans
    }
}
