// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

use std::collections::VecDeque;

impl Solution {
    pub fn cat_mouse_game(graph: Vec<Vec<i32>>) -> i32 {
        const DRAW: i32 = 0;
        const MOUSE_WIN: i32 = 1;
        const CAT_WIN: i32 = 2;
        let n = graph.len();
        let mut states = vec![vec![vec![DRAW; 2]; n]; n];
        let mut out_degree = vec![vec![vec![0; 2]; n]; n];
        let mut q = VecDeque::new();
        for cat in 0..n {
            for mouse in 0..n {
                out_degree[cat][mouse][0] = graph[mouse].len() as i32;
                let deg = graph[cat].iter().filter(|&&x| x != 0).count() as i32;
                out_degree[cat][mouse][1] = deg;
            }
        }
        for cat in 1..n {
            for mv in 0..2 {
                states[cat][0][mv] = MOUSE_WIN;
                q.push_back((cat, 0, mv, MOUSE_WIN));
                states[cat][cat][mv] = CAT_WIN;
                q.push_back((cat, cat, mv, CAT_WIN));
            }
        }
        while let Some((cat, mouse, mv, state)) = q.pop_front() {
            if cat == 2 && mouse == 1 && mv == 0 {
                return state;
            }
            let prev_move = mv ^ 1;
            let prevs = if prev_move == 1 { &graph[cat] } else { &graph[mouse] };
            for &prev in prevs {
                let prev = prev as usize;
                let prev_cat = if prev_move == 1 { prev } else { cat };
                if prev_cat == 0 {
                    continue;
                }
                let prev_mouse = if prev_move == 1 { mouse } else { prev };
                if states[prev_cat][prev_mouse][prev_move] != 0 {
                    continue;
                }
                if (prev_move == 0 && state == MOUSE_WIN)
                    || (prev_move == 1 && state == CAT_WIN)
                    || out_degree[prev_cat][prev_mouse][prev_move] == 1
                {
                    states[prev_cat][prev_mouse][prev_move] = state;
                    q.push_back((prev_cat, prev_mouse, prev_move, state));
                } else {
                    out_degree[prev_cat][prev_mouse][prev_move] -= 1;
                }
            }
        }
        states[2][1][0]
    }
}
