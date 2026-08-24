struct Solution;
// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

impl Solution {
    pub fn dominant_indices(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        let mut suf = nums[n - 1] as i64;
        for i in (0..n - 1).rev() {
            if nums[i] as i64 * (n - i - 1) as i64 > suf {
                ans += 1;
            }
            suf += nums[i] as i64;
        }
        ans
    }
}
