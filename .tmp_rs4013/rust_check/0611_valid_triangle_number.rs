struct Solution;
// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

impl Solution {
    pub fn triangle_number(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut count = 0;
        for k in (2..n).rev() {
            let mut left = 0;
            let mut right = k - 1;
            while left < right {
                if nums[left] + nums[right] > nums[k] {
                    count += (right - left) as i32;
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
        count
    }
}

fn main() {}
