// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn min_flips(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut start = 0;
        for r in 0..m {
            for c in 0..n {
                start |= mat[r][c] << (r * n + c);
            }
        }
        let mut masks = Vec::new();
        for r in 0..m {
            for c in 0..n {
                let mut mask = 0;
                for (dr, dc) in [(0isize, 0), (1, 0), (-1, 0), (0, 1), (0, -1)] {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                        mask ^= 1 << (nr as usize * n + nc as usize);
                    }
                }
                masks.push(mask);
            }
        }
        let mut q = VecDeque::new();
        q.push_back((start, 0));
        let mut seen = HashSet::new();
        seen.insert(start);
        while let Some((state, dist)) = q.pop_front() {
            if state == 0 {
                return dist;
            }
            for &mask in &masks {
                let nxt = state ^ mask;
                if seen.insert(nxt) {
                    q.push_back((nxt, dist + 1));
                }
            }
        }
        -1
    }
}
