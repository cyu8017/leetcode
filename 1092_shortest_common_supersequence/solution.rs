// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

impl Solution {
    pub fn shortest_common_supersequence(str1: String, str2: String) -> String {
        let m = str1.len();
        let n = str2.len();
        let a = str1.as_bytes();
        let b = str2.as_bytes();
        let mut dp = vec![vec![0usize; n + 1]; m + 1];
        for i in 1..=m {
            for j in 1..=n {
                if a[i - 1] == b[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]);
                }
            }
        }
        let mut i = m;
        let mut j = n;
        let mut chars = Vec::new();
        while i > 0 && j > 0 {
            if a[i - 1] == b[j - 1] {
                chars.push(a[i - 1]);
                i -= 1;
                j -= 1;
            } else if dp[i - 1][j] >= dp[i][j - 1] {
                chars.push(a[i - 1]);
                i -= 1;
            } else {
                chars.push(b[j - 1]);
                j -= 1;
            }
        }
        while i > 0 {
            chars.push(a[i - 1]);
            i -= 1;
        }
        while j > 0 {
            chars.push(b[j - 1]);
            j -= 1;
        }
        chars.reverse();
        String::from_utf8(chars).unwrap()
    }
}
