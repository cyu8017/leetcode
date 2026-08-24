struct Solution;
// LeetCode 3912 - Valid Elements in an Array
// https://leetcode.com/problems/valid-elements-in-an-array/

impl Solution {
    pub fn find_valid_elements(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut right = vec![0; n];
        right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right[i] = right[i + 1].max(nums[i]);
        }
        let mut left = 0;
        let mut ans = Vec::new();
        for i in 0..n {
            let x = nums[i];
            if x > left || i == n - 1 || x > right[i + 1] {
                ans.push(x);
            }
            left = left.max(x);
        }
        ans
    }
}
