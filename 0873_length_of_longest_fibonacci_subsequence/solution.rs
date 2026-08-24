// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

use std::collections::HashMap;

impl Solution {
    pub fn len_longest_fib_subseq(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut index = HashMap::new();
        for (i, &x) in arr.iter().enumerate() {
            index.insert(x, i);
        }
        let mut dp = vec![vec![2; n]; n];
        let mut ans = 0;
        for j in 0..n {
            for i in 0..j {
                if let Some(&k) = index.get(&(arr[j] - arr[i])) {
                    if k < i {
                        dp[i][j] = dp[k][i] + 1;
                        ans = ans.max(dp[i][j]);
                    }
                }
            }
        }
        if ans >= 3 {
            ans
        } else {
            0
        }
    }
}
