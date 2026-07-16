// LeetCode 0417 - Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/

impl Solution {
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if heights.is_empty() || heights[0].is_empty() {
            return Vec::new();
        }

        let rows = heights.len();
        let cols = heights[0].len();
        let mut pacific = vec![vec![false; cols]; rows];
        let mut atlantic = vec![vec![false; cols]; rows];

        fn dfs(
            heights: &[Vec<i32>],
            visited: &mut [Vec<bool>],
            row: usize,
            col: usize,
            previous: i32,
        ) {
            if row >= heights.len()
                || col >= heights[0].len()
                || visited[row][col]
                || heights[row][col] < previous
            {
                return;
            }
            visited[row][col] = true;
            let height = heights[row][col];
            if row + 1 < heights.len() {
                dfs(heights, visited, row + 1, col, height);
            }
            if row > 0 {
                dfs(heights, visited, row - 1, col, height);
            }
            if col + 1 < heights[0].len() {
                dfs(heights, visited, row, col + 1, height);
            }
            if col > 0 {
                dfs(heights, visited, row, col - 1, height);
            }
        }

        for row in 0..rows {
            dfs(&heights, &mut pacific, row, 0, heights[row][0]);
            dfs(&heights, &mut atlantic, row, cols - 1, heights[row][cols - 1]);
        }
        for col in 0..cols {
            dfs(&heights, &mut pacific, 0, col, heights[0][col]);
            dfs(&heights, &mut atlantic, rows - 1, col, heights[rows - 1][col]);
        }

        let mut result = Vec::new();
        for row in 0..rows {
            for col in 0..cols {
                if pacific[row][col] && atlantic[row][col] {
                    result.push(vec![row as i32, col as i32]);
                }
            }
        }
        result
    }
}
