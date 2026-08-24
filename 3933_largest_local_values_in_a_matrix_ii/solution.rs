// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

impl Solution {
    pub fn count_local_maximums(matrix: Vec<Vec<i32>>) -> i32 {
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut positions = vec![Vec::new(); 201];
        for row in 0..rows {
            for col in 0..cols {
                let value = matrix[row][col];
                if value > 0 {
                    positions[value as usize].push((row, col));
                }
            }
        }
        let mut answer = 0;
        for value in 1..=200 {
            if positions[value].is_empty() {
                continue;
            }
            let mut prefix = vec![vec![0; cols + 1]; rows + 1];
            for row in 0..rows {
                for col in 0..cols {
                    let add = if matrix[row][col] > value as i32 { 1 } else { 0 };
                    prefix[row + 1][col + 1] =
                        prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add;
                }
            }
            for &(row, col) in &positions[value] {
                let top = row.saturating_sub(value);
                let bottom = (rows - 1).min(row + value);
                let left = col.saturating_sub(value);
                let right = (cols - 1).min(col + value);
                let mut greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1]
                    - prefix[bottom + 1][left]
                    + prefix[top][left];
                for dr in [-(value as i32), value as i32] {
                    for dc in [-(value as i32), value as i32] {
                        let rr = row as i32 + dr;
                        let cc = col as i32 + dc;
                        if rr >= 0
                            && (rr as usize) < rows
                            && cc >= 0
                            && (cc as usize) < cols
                            && matrix[rr as usize][cc as usize] > value as i32
                        {
                            greater -= 1;
                        }
                    }
                }
                if greater == 0 {
                    answer += 1;
                }
            }
        }
        answer
    }
}
