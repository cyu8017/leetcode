// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

impl Solution {
    pub fn valid_tic_tac_toe(board: Vec<String>) -> bool {
        let flat: String = board.concat();
        let x_count = flat.chars().filter(|&ch| ch == 'X').count() as i32;
        let o_count = flat.chars().filter(|&ch| ch == 'O').count() as i32;
        if o_count != x_count && o_count != x_count - 1 {
            return false;
        }
        let x_win = Self::win(&board, 'X');
        let o_win = Self::win(&board, 'O');
        if x_win && o_win {
            return false;
        }
        if x_win && x_count != o_count + 1 {
            return false;
        }
        if o_win && x_count != o_count {
            return false;
        }
        true
    }

    fn win(board: &[String], player: char) -> bool {
        let rows: Vec<Vec<char>> = board.iter().map(|r| r.chars().collect()).collect();
        let target: String = std::iter::repeat(player).take(3).collect();
        for row in board {
            if *row == target {
                return true;
            }
        }
        for c in 0..3 {
            if rows[0][c] == player && rows[1][c] == player && rows[2][c] == player {
                return true;
            }
        }
        if rows[0][0] == player && rows[1][1] == player && rows[2][2] == player {
            return true;
        }
        if rows[0][2] == player && rows[1][1] == player && rows[2][0] == player {
            return true;
        }
        false
    }
}
