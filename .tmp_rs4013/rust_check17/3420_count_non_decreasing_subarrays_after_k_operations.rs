struct Solution;
// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

impl Solution {
    pub fn count_non_decreasing_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            let mut cost = 0i64;
            let mut max_v = nums[i];
            for j in i..n {
                if nums[j] >= max_v {
                    max_v = nums[j];
                } else {
                    cost += (max_v - nums[j]) as i64;
                }
                if cost > k as i64 {
                    break;
                }
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
