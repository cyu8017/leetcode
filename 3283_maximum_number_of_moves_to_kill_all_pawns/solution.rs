// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

use std::collections::{HashMap, VecDeque};

impl Solution {
    fn knight_dist(x: i32, y: i32, pts: &[[i32; 2]]) -> Vec<i32> {
        const DIRS: [[i32; 2]; 8] = [
            [1, 2], [1, -2], [-1, 2], [-1, -2],
            [2, 1], [2, -1], [-2, 1], [-2, -1],
        ];
        let np = pts.len();
        let mut ans = vec![-1; np];
        let mut vis = [[false; 50]; 50];
        let mut q = VecDeque::new();
        q.push_back([x, y, 0]);
        vis[x as usize][y as usize] = true;
        let mut need: HashMap<(i32, i32), Vec<usize>> = HashMap::new();
        for i in 0..np {
            need.entry((pts[i][0], pts[i][1])).or_default().push(i);
        }
        let mut found = 0;
        while !q.is_empty() && found < np {
            let cur = q.pop_front().unwrap();
            let key = (cur[0], cur[1]);
            if let Some(idxs) = need.get(&key) {
                for &i in idxs {
                    if ans[i] == -1 {
                        ans[i] = cur[2];
                        found += 1;
                    }
                }
            }
            for d in &DIRS {
                let nx = cur[0] + d[0];
                let ny = cur[1] + d[1];
                if nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx as usize][ny as usize] {
                    continue;
                }
                vis[nx as usize][ny as usize] = true;
                q.push_back([nx, ny, cur[2] + 1]);
            }
        }
        ans
    }

    pub fn max_moves(kx: i32, ky: i32, positions: Vec<Vec<i32>>) -> i32 {
        let n = positions.len();
        let mut pts = vec![[0; 2]; n + 1];
        pts[0] = [kx, ky];
        for i in 0..n {
            pts[i + 1] = [positions[i][0], positions[i][1]];
        }
        let mut dist = vec![Vec::new(); n + 1];
        for i in 0..=n {
            dist[i] = Self::knight_dist(pts[i][0], pts[i][1], &pts);
        }
        let nmask = 1 << n;
        let mut memo = vec![vec![-1; n + 1]; nmask];
        fn dfs(
            mask: usize,
            cur: usize,
            turn: i32,
            n: usize,
            nmask: usize,
            dist: &[Vec<i32>],
            memo: &mut [Vec<i32>],
        ) -> i32 {
            if mask == nmask - 1 {
                return 0;
            }
            if memo[mask][cur] != -1 {
                return memo[mask][cur];
            }
            let mut best = if turn == 0 { -(1 << 30) } else { 1 << 30 };
            for i in 0..n {
                if mask & (1 << i) != 0 {
                    continue;
                }
                let d = dist[cur][i + 1];
                let v = d + dfs(mask | (1 << i), i + 1, 1 - turn, n, nmask, dist, memo);
                if turn == 0 {
                    if v > best {
                        best = v;
                    }
                } else if v < best {
                    best = v;
                }
            }
            memo[mask][cur] = best;
            best
        }
        dfs(0, 0, 0, n, nmask, &dist, &mut memo)
    }
}
