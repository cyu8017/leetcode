struct Solution;
// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        let mut ans = 0;
        let mut left = 0;
        for i in 0..nums.len() - 1 {
            left += nums[i];
            if (left - (total - left)) % 2 == 0 {
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
