// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

impl Solution {
    pub fn valid_subarray_split(nums: Vec<i32>) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let n = nums.len();
        const INF: i32 = 1 << 30;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        for i in 0..n {
            if dp[i] >= INF {
                continue;
            }
            for j in i..n {
                if gcd(nums[i], nums[j]) > 1 && dp[i] + 1 < dp[j + 1] {
                    dp[j + 1] = dp[i] + 1;
                }
            }
        }
        if dp[n] >= INF {
            -1
        } else {
            dp[n]
        }
    }
}
