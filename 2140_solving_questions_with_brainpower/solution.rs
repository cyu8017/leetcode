// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        let n = questions.len();
        let mut dp = vec![0i64; n + 1];
        for i in (0..n).rev() {
            let pts = questions[i][0] as i64;
            let brain = questions[i][1] as usize;
            let next = i + brain + 1;
            let take = pts + if next < n { dp[next] } else { 0 };
            dp[i] = dp[i + 1].max(take);
        }
        dp[0]
    }
}
