// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, multipliers: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = multipliers.len();
        let mut next = vec![0i32; m + 1];
        for i in (0..m).rev() {
            let mut cur = vec![0i32; m + 1];
            for left in (0..=i).rev() {
                let right = n - 1 - (i - left);
                let take_left = nums[left] * multipliers[i] + next[left + 1];
                let take_right = nums[right] * multipliers[i] + next[left];
                cur[left] = take_left.max(take_right);
            }
            next = cur;
        }
        next[0]
    }
}
