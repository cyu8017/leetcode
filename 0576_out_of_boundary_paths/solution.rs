// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = m as usize;
        let n = n as usize;
        let mut dp = vec![vec![0i32; n]; m];
        dp[start_row as usize][start_column as usize] = 1;
        let mut result = 0;
        let dirs = [(0isize, 1isize), (0, -1), (1, 0), (-1, 0)];
        for _ in 0..max_move {
            let mut nxt = vec![vec![0i32; n]; m];
            for row in 0..m {
                for col in 0..n {
                    let ways = dp[row][col];
                    if ways == 0 {
                        continue;
                    }
                    for (dr, dc) in dirs {
                        let nr = row as isize + dr;
                        let nc = col as isize + dc;
                        if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                            nxt[nr as usize][nc as usize] = (nxt[nr as usize][nc as usize] + ways) % MOD;
                        } else {
                            result = (result + ways) % MOD;
                        }
                    }
                }
            }
            dp = nxt;
        }
        result
    }
}
