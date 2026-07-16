// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

impl Solution {
    pub fn update_board(board: &mut Vec<Vec<char>>, click: Vec<i32>) -> Vec<Vec<char>> {
        let rows = board.len();
        let cols = board[0].len();
        let row = click[0] as usize;
        let col = click[1] as usize;
        let directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];

        if board[row][col] == 'M' {
            board[row][col] = 'X';
            return board.clone();
        }

        fn count_mines(board: &[Vec<char>], row: usize, col: usize, directions: &[(i32, i32)]) -> i32 {
            let rows = board.len();
            let cols = board[0].len();
            let mut total = 0;
            for (dr, dc) in directions {
                let nr = row as i32 + dr;
                let nc = col as i32 + dc;
                if nr >= 0
                    && nr < rows as i32
                    && nc >= 0
                    && nc < cols as i32
                    && board[nr as usize][nc as usize] == 'M'
                {
                    total += 1;
                }
            }
            total
        }

        fn reveal(board: &mut Vec<Vec<char>>, row: usize, col: usize, directions: &[(i32, i32)]) {
            let rows = board.len();
            let cols = board[0].len();
            if row >= rows || col >= cols || board[row][col] != 'E' {
                return;
            }
            let mines = count_mines(board, row, col, directions);
            if mines == 0 {
                board[row][col] = 'B';
                for (dr, dc) in directions {
                    reveal(
                        board,
                        (row as i32 + dr) as usize,
                        (col as i32 + dc) as usize,
                        directions,
                    );
                }
            } else {
                board[row][col] = char::from_digit(mines as u32, 10).unwrap();
            }
        }

        reveal(board, row, col, &directions);
        board.clone()
    }
}
