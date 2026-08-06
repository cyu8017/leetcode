// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        const IMP: i64 = i64::MIN / 4;
        let mut dp = [0i64, IMP, IMP];
        for value in nums {
            let old = dp;
            for total in old {
                if total == IMP {
                    continue;
                }
                let rem = ((total + value as i64) % 3 + 3) % 3;
                dp[rem as usize] = dp[rem as usize].max(total + value as i64);
            }
        }
        dp[0] as i32
    }
}
