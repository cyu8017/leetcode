struct Solution;
// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

impl Solution {
    pub fn array_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        nums.iter().step_by(2).sum()
    }
}

fn main() {}
