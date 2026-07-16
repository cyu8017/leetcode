// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

impl Solution {
    pub fn total_hamming_distance(nums: Vec<i32>) -> i32 {
        let mut total = 0;
        for bit in 0..32 {
            let mut zeros = 0;
            let mut ones = 0;
            for value in &nums {
                if value & (1 << bit) != 0 {
                    ones += 1;
                } else {
                    zeros += 1;
                }
            }
            total += zeros * ones;
        }
        total as i32
    }
}
