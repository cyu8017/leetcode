#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

impl Solution {
    pub fn max_frequency_score(mut nums: Vec<i32>, k: i64) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let cost = |l: usize, r: usize| -> i64 {
            let mid = (l + r) / 2;
            let left = nums[mid] as i64 * (mid - l) as i64 - (pref[mid] - pref[l]);
            let right = (pref[r + 1] - pref[mid + 1]) - nums[mid] as i64 * (r - mid) as i64;
            left + right
        };
        let mut ans = 1;
        let mut left = 0;
        for right in 0..n {
            while cost(left, right) > k {
                left += 1;
            }
            ans = ans.max((right - left + 1) as i32);
        }
        ans
    }
}
