struct Solution;
// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let n = nums1.len();
        let m = nums2.len();
        let kk = k as usize;
        const NEG: i64 = i64::MIN / 4;
        let mut f = vec![vec![vec![NEG; kk + 1]; m + 1]; n + 1];
        f[0][0][0] = 0;
        for i in 0..=n {
            for j in 0..=m {
                for t in 0..=kk {
                    if i > 0 {
                        f[i][j][t] = f[i][j][t].max(f[i - 1][j][t]);
                    }
                    if j > 0 {
                        f[i][j][t] = f[i][j][t].max(f[i][j - 1][t]);
                    }
                    if i > 0 && j > 0 && t > 0 {
                        f[i][j][t] = f[i][j][t]
                            .max(f[i - 1][j - 1][t - 1] + nums1[i - 1] as i64 * nums2[j - 1] as i64);
                    }
                }
            }
        }
        f[n][m][kk]
    }
}
