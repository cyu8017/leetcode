// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

impl Solution {
    pub fn minimum_lines(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        if n <= 2 {
            return 1;
        }
        let colinear = |a: &[i32], b: &[i32], c: &[i32]| {
            (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])
        };
        let inf = n as i32;
        let mut dp = vec![inf; 1 << n];
        dp[0] = 0;
        for mask in 0..(1 << n) {
            if dp[mask] == inf {
                continue;
            }
            let mut i = 0;
            while i < n && (mask & (1 << i)) != 0 {
                i += 1;
            }
            if i == n {
                continue;
            }
            let nm = mask | (1 << i);
            dp[nm] = dp[nm].min(dp[mask] + 1);
            for j in (i + 1)..n {
                if (mask & (1 << j)) != 0 {
                    continue;
                }
                let mut nm = mask | (1 << i) | (1 << j);
                for k in 0..n {
                    if (nm & (1 << k)) == 0 && colinear(&points[i], &points[j], &points[k]) {
                        nm |= 1 << k;
                    }
                }
                dp[nm] = dp[nm].min(dp[mask] + 1);
            }
        }
        dp[(1 << n) - 1]
    }
}
