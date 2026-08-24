struct Solution;
// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

impl Solution {
    pub fn max_adjacent_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let d = (nums[i] - nums[(i + 1) % n]).abs();
            if d > ans {
                ans = d;
            }
        }
        ans
    }
}

fn main() {}
