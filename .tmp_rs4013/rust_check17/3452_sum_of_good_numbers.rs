struct Solution;
// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

impl Solution {
    pub fn sum_of_good_numbers(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut ans = 0;
        for i in 0..n {
            let x = nums[i];
            let mut good = true;
            if i >= k && x <= nums[i - k] {
                good = false;
            }
            if i + k < n && x <= nums[i + k] {
                good = false;
            }
            if good {
                ans += x;
            }
        }
        ans
    }
}

fn main() {}
