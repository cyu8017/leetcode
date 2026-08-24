// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

impl Solution {
    pub fn hit_bricks(grid: Vec<Vec<i32>>, hits: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();
        let roof = m * n;
        let mut parent: Vec<usize> = (0..=roof).collect();
        let mut size = vec![1i32; roof + 1];

        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }

        fn unite(parent: &mut [usize], size: &mut [i32], a: usize, b: usize) {
            let ra = find(parent, a);
            let rb = find(parent, b);
            if ra == rb {
                return;
            }
            parent[ra] = rb;
            size[rb] += size[ra];
        }

        let idx = |r: usize, c: usize| r * n + c;
        let mut status = grid.clone();
        for hit in &hits {
            status[hit[0] as usize][hit[1] as usize] = 0;
        }

        let dr = [-1i32, 1, 0, 0];
        let dc = [0i32, 0, -1, 1];

        for r in 0..m {
            for c in 0..n {
                if status[r][c] == 0 {
                    continue;
                }
                if r == 0 {
                    unite(&mut parent, &mut size, idx(r, c), roof);
                }
                for k in 0..4 {
                    let nr = r as i32 + dr[k];
                    let nc = c as i32 + dc[k];
                    if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                        let (nr, nc) = (nr as usize, nc as usize);
                        if status[nr][nc] == 1 {
                            unite(&mut parent, &mut size, idx(r, c), idx(nr, nc));
                        }
                    }
                }
            }
        }

        let mut answer = vec![0; hits.len()];
        for i in (0..hits.len()).rev() {
            let r = hits[i][0] as usize;
            let c = hits[i][1] as usize;
            if grid[r][c] == 0 {
                continue;
            }
            let prev = size[find(&mut parent, roof)];
            status[r][c] = 1;
            if r == 0 {
                unite(&mut parent, &mut size, idx(r, c), roof);
            }
            for k in 0..4 {
                let nr = r as i32 + dr[k];
                let nc = c as i32 + dc[k];
                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if status[nr][nc] == 1 {
                        unite(&mut parent, &mut size, idx(r, c), idx(nr, nc));
                    }
                }
            }
            let curr = size[find(&mut parent, roof)];
            answer[i] = (curr - prev - 1).max(0);
        }
        answer
    }
}
