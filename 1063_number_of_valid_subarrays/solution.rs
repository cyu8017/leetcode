// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

impl Solution {
    pub fn valid_subarrays(nums: Vec<i32>) -> i32 {
        let mut stack: Vec<usize> = Vec::new();
        let mut ans = 0i32;
        for (i, &x) in nums.iter().enumerate() {
            while stack.last().map(|&j| nums[j] > x).unwrap_or(false) {
                let j = stack.pop().unwrap();
                ans += (i - j) as i32;
            }
            stack.push(i);
        }
        while let Some(j) = stack.pop() {
            ans += (nums.len() - j) as i32;
        }
        ans
    }
}
