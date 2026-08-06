// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

impl Solution {
    pub fn minimum_moves(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut dp = vec![vec![0; n]; n];
        for i in 0..n {
            dp[i][i] = 1;
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                dp[i][j] = 1 + dp[i + 1][j];
                if arr[i] == arr[i + 1] {
                    let mut v = 1;
                    if i + 2 <= j {
                        v += dp[i + 2][j];
                    }
                    dp[i][j] = dp[i][j].min(v);
                }
                for k in i + 2..=j {
                    if arr[i] == arr[k] {
                        let mut v = dp[i + 1][k - 1];
                        if k < j {
                            v += dp[k + 1][j];
                        }
                        dp[i][j] = dp[i][j].min(v);
                    }
                }
            }
        }
        dp[0][n - 1]
    }
}
