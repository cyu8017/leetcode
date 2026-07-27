// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

use std::collections::HashMap;

impl Solution {
    pub fn matrix_rank_transform(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut groups: HashMap<i32, Vec<(usize, usize)>> = HashMap::new();
        for i in 0..m {
            for j in 0..n {
                groups.entry(matrix[i][j]).or_default().push((i, j));
            }
        }
        let mut vals: Vec<i32> = groups.keys().copied().collect();
        vals.sort_unstable();
        let mut rank = vec![0i32; m + n];
        let mut ans = vec![vec![0; n]; m];
        for value in vals {
            let cells = &groups[&value];
            let mut parent: HashMap<usize, usize> = HashMap::new();
            let find = |parent: &mut HashMap<usize, usize>, x: usize| -> usize {
                parent.entry(x).or_insert(x);
                let mut root = x;
                while parent[&root] != root {
                    root = parent[&root];
                }
                let mut cur = x;
                while parent[&cur] != root {
                    let next = parent[&cur];
                    parent.insert(cur, root);
                    cur = next;
                }
                root
            };
            for &(i, j) in cells {
                let a = find(&mut parent, i);
                let b = find(&mut parent, m + j);
                parent.insert(a, b);
            }
            let mut best: HashMap<usize, i32> = HashMap::new();
            for &(i, j) in cells {
                let r = find(&mut parent, i);
                let cur = rank[i].max(rank[m + j]);
                let e = best.entry(r).or_insert(0);
                *e = (*e).max(cur);
            }
            for &(i, j) in cells {
                let r = best[&find(&mut parent, i)] + 1;
                ans[i][j] = r;
            }
            for &(i, j) in cells {
                rank[i] = rank[i].max(ans[i][j]);
                rank[m + j] = rank[m + j].max(ans[i][j]);
            }
        }
        ans
    }
}
