// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

use std::collections::VecDeque;

impl Solution {
    fn bfs(forest: &[Vec<i32>], sr: usize, sc: usize, tr: usize, tc: usize) -> i32 {
        if sr == tr && sc == tc {
            return 0;
        }
        let m = forest.len();
        let n = forest[0].len();
        let mut seen = vec![vec![false; n]; m];
        let mut queue = VecDeque::new();
        queue.push_back((sr, sc, 0));
        seen[sr][sc] = true;
        let dirs = [(-1isize, 0isize), (1, 0), (0, -1), (0, 1)];
        while let Some((r, c, dist)) = queue.pop_front() {
            for (dr, dc) in dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                if seen[nr][nc] || forest[nr][nc] == 0 {
                    continue;
                }
                if nr == tr && nc == tc {
                    return dist + 1;
                }
                seen[nr][nc] = true;
                queue.push_back((nr, nc, dist + 1));
            }
        }
        -1
    }

    pub fn cut_off_tree(forest: Vec<Vec<i32>>) -> i32 {
        let mut trees = Vec::new();
        for i in 0..forest.len() {
            for j in 0..forest[0].len() {
                if forest[i][j] > 1 {
                    trees.push((forest[i][j], i, j));
                }
            }
        }
        trees.sort_unstable();
        let mut sr = 0;
        let mut sc = 0;
        let mut steps = 0;
        for (_, tr, tc) in trees {
            let dist = Self::bfs(&forest, sr, sc, tr, tc);
            if dist < 0 {
                return -1;
            }
            steps += dist;
            sr = tr;
            sc = tc;
        }
        steps
    }
}
