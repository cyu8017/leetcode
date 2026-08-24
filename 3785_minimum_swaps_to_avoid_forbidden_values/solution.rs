// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

use std::collections::HashMap;

impl Solution {
    pub fn min_swaps(nums: Vec<i32>, forbidden: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        for &x in &forbidden {
            *freq.entry(x).or_insert(0) += 1;
        }
        for &c in freq.values() {
            if c > n {
                return -1;
            }
        }
        let mut bad: HashMap<i32, i32> = HashMap::new();
        let mut total = 0;
        let mut largest = 0;
        for i in 0..nums.len() {
            if nums[i] == forbidden[i] {
                let e = bad.entry(nums[i]).or_insert(0);
                *e += 1;
                total += 1;
                if *e > largest {
                    largest = *e;
                }
            }
        }
        if (total + 1) / 2 > largest {
            (total + 1) / 2
        } else {
            largest
        }
    }
}
