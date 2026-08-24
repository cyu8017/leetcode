// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

impl Solution {
    pub fn max_score(a: Vec<i32>, b: Vec<i32>) -> i64 {
        const NEG: i64 = -(1i64 << 62);
        let mut dp = [0i64, NEG, NEG, NEG, NEG];
        for &x in &b {
            for k in (1..=4).rev() {
                if dp[k - 1] == NEG {
                    continue;
                }
                let v = dp[k - 1] + a[k - 1] as i64 * x as i64;
                if v > dp[k] {
                    dp[k] = v;
                }
            }
        }
        dp[4]
    }
}
