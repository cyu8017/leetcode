// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

use std::collections::VecDeque;

impl Solution {
    pub fn snakes_and_ladders(board: Vec<Vec<i32>>) -> i32 {
        let n = board.len() as i32;
        let target = n * n;
        let pos = |square: i32| {
            let square = square - 1;
            let row = square / n;
            let rem = square % n;
            let r = n - 1 - row;
            let c = if row % 2 == 0 { rem } else { n - 1 - rem };
            (r as usize, c as usize)
        };
        let mut q = VecDeque::new();
        let mut seen = vec![false; (target + 1) as usize];
        q.push_back(1);
        seen[1] = true;
        let mut moves = 0;
        while !q.is_empty() {
            let sz = q.len();
            for _ in 0..sz {
                let cur = q.pop_front().unwrap();
                if cur == target {
                    return moves;
                }
                let lim = (cur + 6).min(target);
                for nxt in (cur + 1)..=lim {
                    let (r, c) = pos(nxt);
                    let dest = if board[r][c] != -1 { board[r][c] } else { nxt };
                    if !seen[dest as usize] {
                        seen[dest as usize] = true;
                        q.push_back(dest);
                    }
                }
            }
            moves += 1;
        }
        -1
    }
}
