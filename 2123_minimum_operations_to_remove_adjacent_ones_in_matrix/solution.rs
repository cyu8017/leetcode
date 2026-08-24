// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

impl Solution {
    pub fn minimum_operations(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut id = vec![vec![-1i32; n]; m];
        let mut cnt = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    id[i][j] = cnt;
                    cnt += 1;
                }
            }
        }
        let mut g = vec![Vec::new(); cnt as usize];
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != 1 || (i + j) % 2 != 0 {
                    continue;
                }
                let u = id[i][j] as usize;
                for (di, dj) in dirs {
                    let ni = i as i32 + di;
                    let nj = j as i32 + dj;
                    if ni >= 0 && nj >= 0 && (ni as usize) < m && (nj as usize) < n
                        && grid[ni as usize][nj as usize] == 1
                    {
                        g[u].push(id[ni as usize][nj as usize] as usize);
                    }
                }
            }
        }
        let mut matching = vec![-1i32; cnt as usize];
        fn dfs(u: usize, g: &[Vec<usize>], matching: &mut [i32], seen: &mut [bool]) -> bool {
            for &v in &g[u] {
                if seen[v] {
                    continue;
                }
                seen[v] = true;
                if matching[v] == -1 || dfs(matching[v] as usize, g, matching, seen) {
                    matching[v] = u as i32;
                    return true;
                }
            }
            false
        }
        let mut ans = 0;
        for u in 0..cnt as usize {
            let mut ok = false;
            'outer: for i in 0..m {
                for j in 0..n {
                    if id[i][j] == u as i32 && (i + j) % 2 == 0 {
                        ok = true;
                        break 'outer;
                    }
                }
            }
            if !ok {
                continue;
            }
            let mut seen = vec![false; cnt as usize];
            if dfs(u, &g, &mut matching, &mut seen) {
                ans += 1;
            }
        }
        ans
    }
}
