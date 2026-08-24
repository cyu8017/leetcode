// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

use std::collections::HashMap;

impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut ans = 1;
        for (&t, &f) in &freq {
            let lo = nums.partition_point(|&x| x < t - k);
            let hi = nums.partition_point(|&x| x <= t + k);
            let can = (hi - lo) as i32;
            let mut use_n = can;
            if use_n > f + num_operations {
                use_n = f + num_operations;
            }
            if use_n > ans {
                ans = use_n;
            }
        }
        let mut l = 0;
        for r in 0..n {
            while nums[r] - nums[l] > 2 * k {
                l += 1;
            }
            let mut window = (r - l + 1) as i32;
            if window > num_operations {
                window = num_operations;
            }
            if window > ans {
                ans = window;
            }
        }
        ans
    }
}
