// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

impl Solution {
    pub fn min_moves(classroom: Vec<String>, energy: i32) -> i32 {
        let m = classroom.len();
        let n = classroom[0].len();
        let grid: Vec<Vec<u8>> = classroom.iter().map(|s| s.as_bytes().to_vec()).collect();
        let mut d = vec![vec![0; n]; m];
        let mut x = 0usize;
        let mut y = 0usize;
        let mut cnt = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == b'S' {
                    x = i;
                    y = j;
                } else if grid[i][j] == b'L' {
                    d[i][j] = cnt;
                    cnt += 1;
                }
            }
        }
        if cnt == 0 {
            return 0;
        }
        let energy = energy as usize;
        let mut vis = vec![vec![vec![vec![false; 1 << cnt]; energy + 1]; n]; m];
        let mut q = vec![(x, y, energy, (1 << cnt) - 1)];
        vis[x][y][energy][(1 << cnt) - 1] = true;
        let dirs = [-1i32, 0, 1, 0, -1];
        let mut ans = 0;
        while !q.is_empty() {
            let t = std::mem::take(&mut q);
            for (i, j, cur_energy, mask) in t {
                if mask == 0 {
                    return ans;
                }
                if cur_energy == 0 {
                    continue;
                }
                for k in 0..4 {
                    let nx = i as i32 + dirs[k];
                    let ny = j as i32 + dirs[k + 1];
                    if nx >= 0 && nx < m as i32 && ny >= 0 && ny < n as i32 {
                        let (nx, ny) = (nx as usize, ny as usize);
                        if grid[nx][ny] != b'X' {
                            let nxt_energy = if grid[nx][ny] == b'R' { energy } else { cur_energy - 1 };
                            let mut nxt_mask = mask;
                            if grid[nx][ny] == b'L' {
                                nxt_mask &= !(1 << d[nx][ny]);
                            }
                            if !vis[nx][ny][nxt_energy][nxt_mask] {
                                vis[nx][ny][nxt_energy][nxt_mask] = true;
                                q.push((nx, ny, nxt_energy, nxt_mask));
                            }
                        }
                    }
                }
            }
            ans += 1;
        }
        -1
    }
}
