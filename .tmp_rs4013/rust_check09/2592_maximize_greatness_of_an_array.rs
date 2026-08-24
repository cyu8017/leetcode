struct Solution;

// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

impl Solution {
    pub fn maximize_greatness(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut i = 0;
        for &x in &nums {
            if x > nums[i] {
                i += 1;
            }
        }
        i as i32
    }
}

fn main() {}
