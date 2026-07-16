// LeetCode 0348 - Design Tic-Tac-Toe
// https://leetcode.com/problems/design-tic-tac-toe/

struct TicTacToe {
    n: i32,
    rows: Vec<i32>,
    cols: Vec<i32>,
    diag: i32,
    anti_diag: i32,
}

impl TicTacToe {
    fn new(n: i32) -> Self {
        Self {
            n,
            rows: vec![0; n as usize],
            cols: vec![0; n as usize],
            diag: 0,
            anti_diag: 0,
        }
    }

    fn mov(&mut self, row: i32, col: i32, player: i32) -> i32 {
        let add = if player == 1 { 1 } else { -1 };

        self.rows[row as usize] += add;
        self.cols[col as usize] += add;
        if row == col {
            self.diag += add;
        }
        if row + col == self.n - 1 {
            self.anti_diag += add;
        }

        if self.rows[row as usize].abs() == self.n
            || self.cols[col as usize].abs() == self.n
            || self.diag.abs() == self.n
            || self.anti_diag.abs() == self.n
        {
            return player;
        }

        0
    }
}
