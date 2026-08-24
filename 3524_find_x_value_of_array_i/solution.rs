// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

impl Solution {
    pub fn result_array(nums: Vec<i32>, k: i32) -> Vec<i64> {
        let k = k as usize;
        let mut ans = vec![0i64; k];
        let mut dp = vec![0i64; k];
        for num in nums {
            let mut new_dp = vec![0i64; k];
            let nm = (num as usize) % k;
            new_dp[nm] = 1;
            for i in 0..k {
                new_dp[(i * nm) % k] += dp[i];
            }
            for i in 0..k {
                ans[i] += new_dp[i];
            }
            dp = new_dp;
        }
        ans
    }
}
