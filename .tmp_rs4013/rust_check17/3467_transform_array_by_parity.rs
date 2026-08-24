struct Solution;
// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

impl Solution {
    pub fn transform_array(mut nums: Vec<i32>) -> Vec<i32> {
        for x in nums.iter_mut() {
            *x %= 2;
        }
        let mut j = 0;
        for i in 0..nums.len() {
            if nums[i] == 0 {
                nums.swap(i, j);
                j += 1;
            }
        }
        nums
    }
}

fn main() {}
