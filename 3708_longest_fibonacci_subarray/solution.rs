// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut f = 2;
        let mut ans = f;
        for i in 2..nums.len() {
            if nums[i] == nums[i - 1] + nums[i - 2] {
                f += 1;
                ans = ans.max(f);
            } else {
                f = 2;
            }
        }
        ans
    }
}
