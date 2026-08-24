// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

impl Solution {
    pub fn num_rook_captures(board: Vec<Vec<char>>) -> i32 {
        let m = board.len() as i32;
        let n = board[0].len() as i32;
        let mut r = -1;
        let mut c = -1;
        for i in 0..m {
            for j in 0..n {
                if board[i as usize][j as usize] == 'R' {
                    r = i;
                    c = j;
                }
            }
        }
        if r < 0 {
            return 0;
        }
        let mut ans = 0;
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        for (dr, dc) in dirs {
            let mut i = r + dr;
            let mut j = c + dc;
            while i >= 0 && i < m && j >= 0 && j < n {
                let ch = board[i as usize][j as usize];
                if ch == 'B' {
                    break;
                }
                if ch == 'p' {
                    ans += 1;
                    break;
                }
                i += dr;
                j += dc;
            }
        }
        ans
    }
}
