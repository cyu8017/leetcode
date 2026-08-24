// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

impl Solution {
    pub fn place_word_in_crossword(board: Vec<Vec<char>>, word: String) -> bool {
        let m = board.len();
        let n = board[0].len();
        let w: Vec<char> = word.chars().collect();
        let l = w.len();
        let match_cells = |cells: &[char]| -> bool {
            if cells.len() != l {
                return false;
            }
            let mut ok1 = true;
            let mut ok2 = true;
            for i in 0..l {
                if cells[i] != ' ' && cells[i] != w[i] {
                    ok1 = false;
                }
                if cells[i] != ' ' && cells[i] != w[l - 1 - i] {
                    ok2 = false;
                }
            }
            ok1 || ok2
        };
        for r in 0..m {
            let mut c = 0;
            while c < n {
                while c < n && board[r][c] == '#' {
                    c += 1;
                }
                let start = c;
                while c < n && board[r][c] != '#' {
                    c += 1;
                }
                if c - start == l && match_cells(&board[r][start..c]) {
                    return true;
                }
            }
        }
        for c in 0..n {
            let mut r = 0;
            while r < m {
                while r < m && board[r][c] == '#' {
                    r += 1;
                }
                let start = r;
                while r < m && board[r][c] != '#' {
                    r += 1;
                }
                if r - start == l {
                    let cells: Vec<char> = (0..l).map(|i| board[start + i][c]).collect();
                    if match_cells(&cells) {
                        return true;
                    }
                }
            }
        }
        false
    }
}
