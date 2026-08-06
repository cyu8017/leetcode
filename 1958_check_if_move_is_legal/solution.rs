// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

impl Solution {
    pub fn check_move(board: Vec<Vec<char>>, r_move: i32, c_move: i32, color: char) -> bool {
        let opp = if color == 'B' { 'W' } else { 'B' };
        let dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ];
        for (dr, dc) in dirs {
            let mut r = r_move + dr;
            let mut c = c_move + dc;
            let mut steps = 0;
            while (0..8).contains(&r) && (0..8).contains(&c) && board[r as usize][c as usize] == opp
            {
                r += dr;
                c += dc;
                steps += 1;
            }
            if steps > 0
                && (0..8).contains(&r)
                && (0..8).contains(&c)
                && board[r as usize][c as usize] == color
            {
                return true;
            }
        }
        false
    }
}
