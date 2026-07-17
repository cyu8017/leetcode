// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

impl Solution {
    pub fn find_ball(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len() as i32;
        let mut ans = Vec::with_capacity(n as usize);
        for start in 0..n {
            let mut col = start;
            for row in 0..m {
                let next = col + grid[row][col as usize];
                if next < 0 || next == n || grid[row][next as usize] != grid[row][col as usize] {
                    col = -1;
                    break;
                }
                col = next;
            }
            ans.push(col);
        }
        ans
    }
}
