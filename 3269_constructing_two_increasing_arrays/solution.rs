// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

impl Solution {
    pub fn min_largest(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let m = nums2.len();
        const INF: i32 = 1_000_000_000;
        let mut dp = vec![vec![INF; m + 1]; n + 1];
        dp[0][0] = 0;
        for i in 0..=n {
            for j in 0..=m {
                if dp[i][j] == INF {
                    continue;
                }
                let prev = dp[i][j];
                if i < n {
                    let mut need = prev + 1;
                    if nums1[i] == 0 {
                        if need % 2 != 0 {
                            need += 1;
                        }
                    } else if need % 2 == 0 {
                        need += 1;
                    }
                    if need < dp[i + 1][j] {
                        dp[i + 1][j] = need;
                    }
                }
                if j < m {
                    let mut need = prev + 1;
                    if nums2[j] == 0 {
                        if need % 2 != 0 {
                            need += 1;
                        }
                    } else if need % 2 == 0 {
                        need += 1;
                    }
                    if need < dp[i][j + 1] {
                        dp[i][j + 1] = need;
                    }
                }
            }
        }
        dp[n][m]
    }
}
