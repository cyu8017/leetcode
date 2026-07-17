// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i32 {
        fn gcd(a: i32, b: i32) -> i32 {
            if b == 0 { a } else { gcd(b, a % b) }
        }
        fn dp(mask: usize, n: usize, nums: &[i32], memo: &mut [i32]) -> i32 {
            if mask == (1 << n) - 1 {
                return 0;
            }
            if memo[mask] != -1 {
                return memo[mask];
            }
            let step = (mask.count_ones() / 2 + 1) as i32;
            let mut best = 0;
            for i in 0..n {
                if mask >> i & 1 == 1 {
                    continue;
                }
                for j in i + 1..n {
                    if mask >> j & 1 == 1 {
                        continue;
                    }
                    let score =
                        step * gcd(nums[i], nums[j]) + dp(mask | 1 << i | 1 << j, n, nums, memo);
                    best = best.max(score);
                }
            }
            memo[mask] = best;
            best
        }

        let n = nums.len();
        let mut memo = vec![-1; 1 << n];
        dp(0, n, &nums, &mut memo)
    }
}
