// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

impl Solution {
    pub fn count_elements(mut nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if k == 0 {
            return n as i32;
        }
        nums.sort_unstable();
        let mut ans = 0;
        let k = k as usize;
        if n < k {
            return 0;
        }
        for i in 0..n - k {
            if nums[n - k] > nums[i] {
                ans += 1;
            }
        }
        ans
    }
}
