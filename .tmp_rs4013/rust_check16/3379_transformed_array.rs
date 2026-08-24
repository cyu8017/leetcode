struct Solution;
// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

impl Solution {
    pub fn construct_transformed_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut ans = vec![0; nums.len()];
        for i in 0..nums.len() {
            let j = ((i as i32 + nums[i]) % n + n) % n;
            ans[i] = nums[j as usize];
        }
        ans
    }
}

fn main() {}
