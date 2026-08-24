struct Solution;
// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> bool {
        let n = nums.len();
        let mut diff = vec![0i32; n + 1];
        for q in &queries {
            diff[q[0] as usize] += 1;
            diff[q[1] as usize + 1] -= 1;
        }
        let mut cur = 0;
        for i in 0..n {
            cur += diff[i];
            if cur < nums[i] {
                return false;
            }
        }
        true
    }
}

fn main() {}
