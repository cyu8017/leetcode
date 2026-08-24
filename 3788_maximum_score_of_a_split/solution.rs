// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

impl Solution {
    pub fn maximum_score(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut suf = vec![0i64; n];
        suf[n - 1] = nums[n - 1] as i64;
        for i in (0..n - 1).rev() {
            suf[i] = (nums[i] as i64).min(suf[i + 1]);
        }
        let mut pre = 0i64;
        let mut ans = i64::MIN;
        for i in 0..n - 1 {
            pre += nums[i] as i64;
            ans = ans.max(pre - suf[i + 1]);
        }
        ans
    }
}
