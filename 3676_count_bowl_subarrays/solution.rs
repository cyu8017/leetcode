// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

impl Solution {
    pub fn bowl_subarrays(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        let mut ngr = vec![-1i32; n];
        let mut ngl = vec![-1i32; n];
        let mut stack = Vec::new();
        for i in (0..n).rev() {
            while !stack.is_empty() && nums[*stack.last().unwrap()] < nums[i] {
                stack.pop();
            }
            if let Some(&j) = stack.last() {
                ngr[i] = j as i32;
            }
            stack.push(i);
        }
        stack.clear();
        for i in 0..n {
            while !stack.is_empty() && nums[*stack.last().unwrap()] < nums[i] {
                stack.pop();
            }
            if let Some(&j) = stack.last() {
                ngl[i] = j as i32;
            }
            stack.push(i);
        }
        for i in 0..n {
            if ngr[i] != -1 && ngr[i] - i as i32 >= 2 {
                ans += 1;
            }
            if ngl[i] != -1 && i as i32 - ngl[i] >= 2 {
                ans += 1;
            }
        }
        ans
    }
}
