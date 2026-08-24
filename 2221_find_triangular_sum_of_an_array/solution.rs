// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

impl Solution {
    pub fn triangular_sum(mut nums: Vec<i32>) -> i32 {
        while nums.len() > 1 {
            let next: Vec<i32> = nums.windows(2).map(|w| (w[0] + w[1]) % 10).collect();
            nums = next;
        }
        nums[0]
    }
}
