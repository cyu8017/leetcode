// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

use std::collections::HashMap;

impl Solution {
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {
        let mut prefix: i64 = 0;
        let mut remainders = HashMap::from([(0_i64, -1_i32)]);

        for (index, num) in nums.iter().enumerate() {
            prefix += *num as i64;
            let modulo = if k != 0 { prefix % k as i64 } else { prefix };
            if let Some(&prev) = remainders.get(&modulo) {
                if (index as i32) - prev >= 2 {
                    return true;
                }
            } else {
                remainders.insert(modulo, index as i32);
            }
        }
        false
    }
}
