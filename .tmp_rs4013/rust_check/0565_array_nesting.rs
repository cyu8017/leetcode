struct Solution;
// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

impl Solution {
    pub fn array_nesting(mut nums: Vec<i32>) -> i32 {
        let mut best = 0;
        for i in 0..nums.len() {
            if nums[i] < 0 {
                continue;
            }
            let mut length = 0;
            let mut j = i as i32;
            while nums[j as usize] >= 0 {
                let nxt = nums[j as usize];
                nums[j as usize] = -1;
                j = nxt;
                length += 1;
            }
            best = best.max(length);
        }
        best
    }
}

fn main() {}
