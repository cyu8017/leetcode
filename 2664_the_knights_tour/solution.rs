// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

const DIRS: [(i32, i32); 8] = [
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
];

impl Solution {
    pub fn tour_of_knight(m: i32, n: i32, r: i32, c: i32) -> Vec<Vec<i32>> {
        let m = m as usize;
        let n = n as usize;
        let mut ans = vec![vec![-1; n]; m];
        fn dfs(ans: &mut [Vec<i32>], x: i32, y: i32, step: i32, m: i32, n: i32) -> bool {
            ans[x as usize][y as usize] = step;
            if step == m * n - 1 {
                return true;
            }
            for &(dx, dy) in &DIRS {
                let nx = x + dx;
                let ny = y + dy;
                if nx >= 0
                    && nx < m
                    && ny >= 0
                    && ny < n
                    && ans[nx as usize][ny as usize] == -1
                    && dfs(ans, nx, ny, step + 1, m, n)
                {
                    return true;
                }
            }
            ans[x as usize][y as usize] = -1;
            false
        }
        dfs(&mut ans, r, c, 0, m as i32, n as i32);
        ans
    }
}
