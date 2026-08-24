// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

impl Solution {
    pub fn find_champion(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        for i in 0..n {
            let mut win = true;
            for j in 0..n {
                if i != j && grid[i][j] == 0 {
                    win = false;
                    break;
                }
            }
            if win {
                return i as i32;
            }
        }
        -1
    }
}
