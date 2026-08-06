// LeetCode 1301 - Number of Paths with Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

impl Solution {
    pub fn paths_with_max_score(board: Vec<String>) -> Vec<i32> {
        const MOD: i32 = 1_000_000_007;
        let n = board.len();
        let board: Vec<Vec<u8>> = board.into_iter().map(|s| s.into_bytes()).collect();
        let mut score = vec![vec![-1; n]; n];
        let mut ways = vec![vec![0; n]; n];
        score[n - 1][n - 1] = 0;
        ways[n - 1][n - 1] = 1;
        for r in (0..n).rev() {
            for c in (0..n).rev() {
                if board[r][c] == b'X' || (r == n - 1 && c == n - 1) {
                    continue;
                }
                let mut best = -1;
                let mut count = 0;
                for (nr, nc) in [(r + 1, c), (r, c + 1), (r + 1, c + 1)] {
                    if nr < n && nc < n && score[nr][nc] >= 0 {
                        if score[nr][nc] > best {
                            best = score[nr][nc];
                            count = ways[nr][nc];
                        } else if score[nr][nc] == best {
                            count = (count + ways[nr][nc]) % MOD;
                        }
                    }
                }
                if best >= 0 {
                    let add = if board[r][c].is_ascii_digit() {
                        (board[r][c] - b'0') as i32
                    } else {
                        0
                    };
                    score[r][c] = best + add;
                    ways[r][c] = count;
                }
            }
        }
        vec![score[0][0].max(0), ways[0][0]]
    }
}
