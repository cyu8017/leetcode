// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

use std::collections::HashMap;

#[derive(Clone, Copy)]
struct Move {
    dr: i32,
    dc: i32,
    steps: i32,
}

impl Solution {
    pub fn count_combinations(pieces: Vec<String>, positions: Vec<Vec<i32>>) -> i32 {
        let dirs_map: HashMap<&str, Vec<(i32, i32)>> = [
            ("rook", vec![(1, 0), (-1, 0), (0, 1), (0, -1)]),
            ("bishop", vec![(1, 1), (1, -1), (-1, 1), (-1, -1)]),
            (
                "queen",
                vec![
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                    (1, 1),
                    (1, -1),
                    (-1, 1),
                    (-1, -1),
                ],
            ),
        ]
        .into_iter()
        .collect();
        let n = pieces.len();
        let mut all_moves = vec![Vec::new(); n];
        for i in 0..n {
            let mut ms = vec![Move { dr: 0, dc: 0, steps: 0 }];
            let r = positions[i][0];
            let c = positions[i][1];
            for &(dr, dc) in &dirs_map[pieces[i].as_str()] {
                let mut nr = r + dr;
                let mut nc = c + dc;
                let mut step = 1;
                while nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8 {
                    ms.push(Move { dr, dc, steps: step });
                    nr += dr;
                    nc += dc;
                    step += 1;
                }
            }
            all_moves[i] = ms;
        }
        fn ok_combo(
            end: usize,
            chosen: &[Move],
            positions: &[Vec<i32>],
        ) -> bool {
            let max_t = chosen[..=end].iter().map(|m| m.steps).max().unwrap_or(0);
            for t in 1..=max_t {
                let mut pos = HashMap::new();
                for i in 0..=end {
                    let m = chosen[i];
                    let (pr, pc) = if m.steps == 0 {
                        (positions[i][0], positions[i][1])
                    } else {
                        let use_t = t.min(m.steps);
                        (
                            positions[i][0] + m.dr * use_t,
                            positions[i][1] + m.dc * use_t,
                        )
                    };
                    if pos.contains_key(&(pr, pc)) {
                        return false;
                    }
                    pos.insert((pr, pc), i);
                }
            }
            true
        }
        fn dfs(
            i: usize,
            n: usize,
            all_moves: &[Vec<Move>],
            chosen: &mut [Move],
            positions: &[Vec<i32>],
            ans: &mut i32,
        ) {
            if i == n {
                *ans += 1;
                return;
            }
            for &m in &all_moves[i] {
                chosen[i] = m;
                if ok_combo(i, chosen, positions) {
                    dfs(i + 1, n, all_moves, chosen, positions, ans);
                }
            }
        }
        let mut chosen = vec![Move { dr: 0, dc: 0, steps: 0 }; n];
        let mut ans = 0;
        dfs(0, n, &all_moves, &mut chosen, &positions, &mut ans);
        ans
    }
}
