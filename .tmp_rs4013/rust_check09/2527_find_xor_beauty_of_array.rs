struct Solution;

// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

impl Solution {
    pub fn xor_beauty(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for x in nums {
            ans ^= x;
        }
        ans
    }
}

fn main() {}
