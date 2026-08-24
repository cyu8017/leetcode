struct Solution;

// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

impl Solution {
    pub fn maximum_count(nums: Vec<i32>) -> i32 {
        let mut pos = 0;
        let mut neg = 0;
        for x in nums {
            if x > 0 {
                pos += 1;
            } else if x < 0 {
                neg += 1;
            }
        }
        pos.max(neg)
    }
}

fn main() {}
