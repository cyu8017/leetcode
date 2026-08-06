// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

impl Solution {
    pub fn find_maximums(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut left = vec![-1i32; n];
        let mut right = vec![n as i32; n];
        let mut stack: Vec<usize> = Vec::new();
        for (i, &x) in nums.iter().enumerate() {
            while let Some(&top) = stack.last() {
                if nums[top] >= x {
                    stack.pop();
                } else {
                    break;
                }
            }
            left[i] = stack.last().map(|&t| t as i32).unwrap_or(-1);
            stack.push(i);
        }
        stack.clear();
        for i in (0..n).rev() {
            while let Some(&top) = stack.last() {
                if nums[top] >= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            right[i] = stack.last().map(|&t| t as i32).unwrap_or(n as i32);
            stack.push(i);
        }

        let mut ans = vec![0; n];
        for (i, &x) in nums.iter().enumerate() {
            let length = (right[i] - left[i] - 1) as usize;
            ans[length - 1] = ans[length - 1].max(x);
        }
        for i in (0..n - 1).rev() {
            ans[i] = ans[i].max(ans[i + 1]);
        }
        ans
    }
}
