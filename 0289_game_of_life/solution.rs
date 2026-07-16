// LeetCode 0289 - Game of Life
// https://leetcode.com/problems/game-of-life/

impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        if board.is_empty() || board[0].is_empty() {
            return;
        }

        let rows = board.len();
        let cols = board[0].len();

        for row in 0..rows {
            for col in 0..cols {
                let mut live_neighbors = 0;
                for dr in -1..=1 {
                    for dc in -1..=1 {
                        if dr == 0 && dc == 0 {
                            continue;
                        }
                        let next_row = row as i32 + dr;
                        let next_col = col as i32 + dc;
                        if next_row >= 0
                            && next_row < rows as i32
                            && next_col >= 0
                            && next_col < cols as i32
                        {
                            if board[next_row as usize][next_col as usize] & 1 == 1 {
                                live_neighbors += 1;
                            }
                        }
                    }
                }
                if board[row][col] & 1 == 1 && (live_neighbors == 2 || live_neighbors == 3) {
                    board[row][col] |= 2;
                } else if board[row][col] & 1 == 0 && live_neighbors == 3 {
                    board[row][col] |= 2;
                }
            }
        }

        for row in 0..rows {
            for col in 0..cols {
                board[row][col] >>= 1;
            }
        }
    }
}
