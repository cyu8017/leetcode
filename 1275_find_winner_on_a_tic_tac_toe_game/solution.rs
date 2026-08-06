// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

impl Solution {
    pub fn tictactoe(moves: Vec<Vec<i32>>) -> String {
        let mut board = [[0i32; 3]; 3];
        for (i, mv) in moves.iter().enumerate() {
            board[mv[0] as usize][mv[1] as usize] = if i % 2 == 0 { 1 } else { -1 };
        }
        let mut lines = Vec::new();
        for r in 0..3 {
            lines.push([board[r][0], board[r][1], board[r][2]]);
        }
        for c in 0..3 {
            lines.push([board[0][c], board[1][c], board[2][c]]);
        }
        lines.push([board[0][0], board[1][1], board[2][2]]);
        lines.push([board[0][2], board[1][1], board[2][0]]);
        for line in lines {
            let s = line[0] + line[1] + line[2];
            if s == 3 {
                return "A".to_string();
            }
            if s == -3 {
                return "B".to_string();
            }
        }
        if moves.len() == 9 {
            "Draw".to_string()
        } else {
            "Pending".to_string()
        }
    }
}
