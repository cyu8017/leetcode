// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut mn = 1 << 30;
        for i in 0..n {
            left[i] = mn;
            if nums[i] < mn {
                mn = nums[i];
            }
        }
        mn = 1 << 30;
        for i in (0..n).rev() {
            right[i] = mn;
            if nums[i] < mn {
                mn = nums[i];
            }
        }
        let mut ans = 1 << 30;
        for j in 1..n - 1 {
            if left[j] < nums[j] && right[j] < nums[j] {
                ans = ans.min(left[j] + nums[j] + right[j]);
            }
        }
        if ans == (1 << 30) { -1 } else { ans }
    }
}
