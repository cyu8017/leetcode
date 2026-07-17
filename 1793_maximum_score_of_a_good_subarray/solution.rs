// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut stack: Vec<usize> = Vec::new();
        let mut ans: i64 = 0;
        for i in 0..=n {
            while let Some(&top) = stack.last() {
                if i < n && nums[i] >= nums[top] {
                    break;
                }
                let mid = stack.pop().unwrap();
                let left = stack.last().map_or(0, |&j| j + 1);
                let right = i - 1;
                if left <= k && k <= right {
                    ans = ans.max(nums[mid] as i64 * (right - left + 1) as i64);
                }
            }
            stack.push(i);
        }
        ans as i32
    }
}
