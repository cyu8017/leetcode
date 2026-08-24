struct Solution;

// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

impl Solution {
    pub fn find_smallest_integer(nums: Vec<i32>, value: i32) -> i32 {
        let value = value as usize;
        let mut cnt = vec![0; value];
        for x in nums {
            let mut r = x % value as i32;
            if r < 0 {
                r += value as i32;
            }
            cnt[r as usize] += 1;
        }
        let mut mex = 0;
        while cnt[mex % value] > 0 {
            cnt[mex % value] -= 1;
            mex += 1;
        }
        mex as i32
    }
}

fn main() {}
