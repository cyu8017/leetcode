// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

impl Solution {
    pub fn max_size_slices(slices: Vec<i32>) -> i32 {
        let k = slices.len() / 3;
        fn line(a: &[i32], k: usize) -> i32 {
            let n = a.len();
            let mut dp = vec![vec![0; k + 1]; n + 2];
            for (idx, &x) in a.iter().enumerate() {
                let i = idx + 2;
                for j in 1..=k {
                    dp[i][j] = dp[i - 1][j].max(dp[i - 2][j - 1] + x);
                }
            }
            dp[n + 1][k]
        }
        line(&slices[..slices.len() - 1], k).max(line(&slices[1..], k))
    }
}
