// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

impl Solution {
    fn dist_circ(a: u8, b: u8) -> i32 {
        let d = (a as i32 - b as i32).abs();
        d.min(26 - d)
    }

    pub fn longest_palindromic_subsequence(s: String, k: i32) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut dp = vec![vec![vec![-1; (k + 1) as usize]; n]; n];
        fn dfs(
            i: i32,
            j: i32,
            ops: i32,
            bytes: &[u8],
            dp: &mut [Vec<Vec<i32>>],
        ) -> i32 {
            if i > j {
                return 0;
            }
            if i == j {
                return 1;
            }
            let iu = i as usize;
            let ju = j as usize;
            if dp[iu][ju][ops as usize] != -1 {
                return dp[iu][ju][ops as usize];
            }
            let mut best = dfs(i + 1, j, ops, bytes, dp);
            best = best.max(dfs(i, j - 1, ops, bytes, dp));
            let cost = Solution::dist_circ(bytes[iu], bytes[ju]);
            if cost <= ops {
                best = best.max(2 + dfs(i + 1, j - 1, ops - cost, bytes, dp));
            }
            dp[iu][ju][ops as usize] = best;
            best
        }
        dfs(0, n as i32 - 1, k, bytes, &mut dp)
    }
}
