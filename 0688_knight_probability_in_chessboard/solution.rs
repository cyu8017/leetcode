// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

impl Solution {
    pub fn knight_probability(n: i32, k: i32, row: i32, column: i32) -> f64 {
        let n = n as usize;
        let moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ];
        let mut dp = vec![vec![0.0; n]; n];
        dp[row as usize][column as usize] = 1.0;
        for _ in 0..k {
            let mut nxt = vec![vec![0.0; n]; n];
            for r in 0..n {
                for c in 0..n {
                    if dp[r][c] == 0.0 {
                        continue;
                    }
                    for &(dr, dc) in &moves {
                        let nr = r as i32 + dr;
                        let nc = c as i32 + dc;
                        if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {
                            nxt[nr as usize][nc as usize] += dp[r][c] / 8.0;
                        }
                    }
                }
            }
            dp = nxt;
        }
        dp.iter().flatten().sum()
    }
}
