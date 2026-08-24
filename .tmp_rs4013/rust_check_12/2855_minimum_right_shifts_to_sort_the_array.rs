struct Solution;
// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

impl Solution {
    pub fn minimum_right_shifts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut drops = 0;
        let mut idx = 0usize;
        for i in 0..n {
            if nums[i] > nums[(i + 1) % n] {
                drops += 1;
                idx = i;
            }
        }
        if drops == 0 {
            return 0;
        }
        if drops > 1 {
            return -1;
        }
        (n - 1 - idx) as i32
    }
}

fn main() {}
