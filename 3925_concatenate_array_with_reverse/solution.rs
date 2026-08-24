// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

impl Solution {
    pub fn concat_with_reverse(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0; 2 * n];
        for i in 0..n {
            ans[i] = nums[i];
            ans[i + n] = nums[n - i - 1];
        }
        ans
    }
}
