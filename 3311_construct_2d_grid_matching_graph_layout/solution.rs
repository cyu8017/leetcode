// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

impl Solution {
    pub fn construct_grid_layout(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let deg: Vec<usize> = g.iter().map(|v| v.len()).collect();
        let mut start = 0;
        for i in 0..n {
            if deg[i] == 1 {
                start = i;
                break;
            }
            if deg[i] == 2 {
                start = i;
            }
        }
        let mut vis = vec![false; n];
        let mut row = Vec::new();
        let mut cur = start;
        let mut prev = usize::MAX;
        loop {
            row.push(cur);
            vis[cur] = true;
            let mut next = None;
            for &v in &g[cur] {
                if v != prev && !vis[v] && deg[v] <= 3 {
                    next = Some(v);
                    if deg[v] < 4 {
                        break;
                    }
                }
            }
            match next {
                None => break,
                Some(v) => {
                    prev = cur;
                    cur = v;
                }
            }
        }
        let mut width = row.len();
        let mut height = if width != 0 { n / width } else { n };
        if width == 0 || width * height != n {
            for w in 1..=n {
                if n % w == 0 {
                    width = w;
                    height = n / w;
                    break;
                }
            }
        }
        let mut grid = vec![vec![0; width]; height];
        for i in 0..n {
            grid[i / width][i % width] = i as i32;
        }
        grid
    }
}
