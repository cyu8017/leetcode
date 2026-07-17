// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

impl Solution {
    pub fn can_mouse_win(grid: Vec<String>, cat_jump: i32, mouse_jump: i32) -> bool {
        let rows = grid.len();
        let cols = grid[0].len();
        let bytes: Vec<&[u8]> = grid.iter().map(|row| row.as_bytes()).collect();
        let mut total_open = 0usize;
        let mut mouse = 0usize;
        let mut cat = 0usize;
        let mut food = 0usize;
        for r in 0..rows {
            for c in 0..cols {
                let cell = bytes[r][c];
                if cell != b'#' {
                    total_open += 1;
                }
                match cell {
                    b'M' => mouse = r * cols + c,
                    b'C' => cat = r * cols + c,
                    b'F' => food = r * cols + c,
                    _ => {}
                }
            }
        }
        let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        let compute_moves = |pos: usize, jump: i32| -> Vec<usize> {
            let r = (pos / cols) as i32;
            let c = (pos % cols) as i32;
            let mut out = vec![pos];
            for &(dr, dc) in &dirs {
                for step in 1..=jump {
                    let nr = r + dr * step;
                    let nc = c + dc * step;
                    if nr < 0
                        || nr >= rows as i32
                        || nc < 0
                        || nc >= cols as i32
                        || bytes[nr as usize][nc as usize] == b'#'
                    {
                        break;
                    }
                    out.push(nr as usize * cols + nc as usize);
                }
            }
            out
        };
        let cells = rows * cols;
        let mut mouse_moves: Vec<Vec<usize>> = vec![Vec::new(); cells];
        let mut cat_moves: Vec<Vec<usize>> = vec![Vec::new(); cells];
        for r in 0..rows {
            for c in 0..cols {
                if bytes[r][c] != b'#' {
                    let pos = r * cols + c;
                    mouse_moves[pos] = compute_moves(pos, mouse_jump);
                    cat_moves[pos] = compute_moves(pos, cat_jump);
                }
            }
        }
        let max_turn = 2 * total_open;
        let mut memo = vec![0i8; cells * cells * max_turn];

        fn win(
            m: usize,
            c: usize,
            turn: usize,
            food: usize,
            max_turn: usize,
            cells: usize,
            mouse_moves: &[Vec<usize>],
            cat_moves: &[Vec<usize>],
            memo: &mut [i8],
        ) -> bool {
            if turn >= max_turn {
                return false;
            }
            if m == food {
                return true;
            }
            if c == food || c == m {
                return false;
            }
            let key = (m * cells + c) * max_turn + turn;
            if memo[key] != 0 {
                return memo[key] == 1;
            }
            let result = if turn % 2 == 0 {
                mouse_moves[m]
                    .iter()
                    .any(|&nm| win(nm, c, turn + 1, food, max_turn, cells, mouse_moves, cat_moves, memo))
            } else {
                cat_moves[c]
                    .iter()
                    .all(|&nc| win(m, nc, turn + 1, food, max_turn, cells, mouse_moves, cat_moves, memo))
            };
            memo[key] = if result { 1 } else { 2 };
            result
        }

        win(mouse, cat, 0, food, max_turn, cells, &mouse_moves, &cat_moves, &mut memo)
    }
}
