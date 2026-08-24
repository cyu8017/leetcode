struct Solution;
// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        if k == 1 {
            return nums;
        }
        let mut ans = vec![0; n - k + 1];
        let mut streak = 1;
        for i in 1..n {
            if nums[i] == nums[i - 1] + 1 {
                streak += 1;
            } else {
                streak = 1;
            }
            if i >= k - 1 {
                ans[i - k + 1] = if streak >= k { nums[i] } else { -1 };
            }
        }
        ans
    }
}

fn main() {}
