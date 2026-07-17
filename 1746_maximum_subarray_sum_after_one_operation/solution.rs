// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

impl Solution {
    pub fn max_sum_after_operation(nums: Vec<i32>) -> i32 {
        let mut no_square: i64 = 0;
        let mut one_square: i64 = 0;
        let mut best = i64::MIN;
        for &value in &nums {
            let v = value as i64;
            one_square = (one_square + v).max(no_square + v * v).max(v * v);
            no_square = (no_square + v).max(v);
            best = best.max(one_square);
        }
        best as i32
    }
}
