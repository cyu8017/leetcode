// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn get_largest_outlier(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            sum += x;
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut ans = i32::MIN;
        for &x in &nums {
            *freq.get_mut(&x).unwrap() -= 1;
            let rem = sum - x;
            if rem % 2 == 0 {
                let cand = rem / 2;
                if *freq.get(&cand).unwrap_or(&0) > 0 && x > ans {
                    ans = x;
                }
            }
            *freq.get_mut(&x).unwrap() += 1;
        }
        ans
    }
}
