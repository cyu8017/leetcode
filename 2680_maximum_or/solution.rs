// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

impl Solution {
    pub fn maximum_or(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        let mut suf = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] | nums[i] as i64;
        }
        for i in (0..n).rev() {
            suf[i] = suf[i + 1] | nums[i] as i64;
        }
        let mut ans = 0i64;
        for i in 0..n {
            let cur = pref[i] | ((nums[i] as i64) << k) | suf[i + 1];
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
