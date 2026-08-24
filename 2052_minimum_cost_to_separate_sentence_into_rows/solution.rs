// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

impl Solution {
    pub fn minimum_cost(sentence: String, k: i32) -> i32 {
        let words: Vec<&str> = sentence.split_whitespace().collect();
        let n = words.len();
        let mut dp = vec![i64::MAX / 4; n + 1];
        dp[n] = 0;
        for i in (0..n).rev() {
            let mut length = -1;
            for j in i..n {
                length += 1 + words[j].len() as i32;
                if length > k {
                    break;
                }
                let mut cost = 0i64;
                if j < n - 1 {
                    let extra = (k - length) as i64;
                    cost = extra * extra;
                }
                dp[i] = dp[i].min(cost + dp[j + 1]);
            }
        }
        dp[0] as i32
    }
}
