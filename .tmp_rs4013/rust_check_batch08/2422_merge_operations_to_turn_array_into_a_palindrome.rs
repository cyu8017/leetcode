struct Solution;
// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut l = 0usize;
        let mut r = nums.len() - 1;
        let mut left = nums[l] as i64;
        let mut right = nums[r] as i64;
        let mut ans = 0;
        while l < r {
            if left == right {
                l += 1;
                r -= 1;
                if l < r {
                    left = nums[l] as i64;
                    right = nums[r] as i64;
                }
            } else if left < right {
                l += 1;
                left += nums[l] as i64;
                ans += 1;
            } else {
                r -= 1;
                right += nums[r] as i64;
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
