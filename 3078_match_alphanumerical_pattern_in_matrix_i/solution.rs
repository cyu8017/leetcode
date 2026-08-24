// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

impl Solution {
    pub fn find_pattern(board: Vec<Vec<i32>>, pattern: Vec<String>) -> Vec<i32> {
        let m = board.len();
        let n = board[0].len();
        let r = pattern.len();
        let c = pattern[0].len();
        let pats: Vec<Vec<u8>> = pattern.iter().map(|s| s.as_bytes().to_vec()).collect();
        let check = |i: usize, j: usize| -> bool {
            let mut d1 = [0i32; 26];
            let mut d2 = [0i32; 10];
            for a in 0..r {
                for b in 0..c {
                    let x = i + a;
                    let y = j + b;
                    let ch = pats[a][b];
                    if ch.is_ascii_digit() {
                        if (ch - b'0') as i32 != board[x][y] {
                            return false;
                        }
                    } else {
                        let v = (ch - b'a') as usize;
                        let cell = board[x][y] as usize;
                        if d1[v] > 0 && d1[v] - 1 != board[x][y] {
                            return false;
                        }
                        if d2[cell] > 0 && d2[cell] - 1 != v as i32 {
                            return false;
                        }
                        d1[v] = board[x][y] + 1;
                        d2[cell] = v as i32 + 1;
                    }
                }
            }
            true
        };
        for i in 0..=m - r {
            for j in 0..=n - c {
                if check(i, j) {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![-1, -1]
    }
}
