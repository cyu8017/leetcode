struct Solution;

// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        let mut great = vec![0i32; n];
        for j in 0..n {
            for i in 0..j {
                if nums[i] < nums[j] {
                    ans += great[i] as i64;
                } else if nums[i] > nums[j] {
                    great[i] += 1;
                }
            }
        }
        ans
    }
}

fn main() {}
