// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

impl Solution {
    pub fn spiral_matrix_iii(rows: i32, cols: i32, r_start: i32, c_start: i32) -> Vec<Vec<i32>> {
        let mut ans = vec![vec![r_start, c_start]];
        if rows * cols == 1 {
            return ans;
        }
        let mut r = r_start;
        let mut c = c_start;
        let dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        let mut steps = 1;
        while (ans.len() as i32) < rows * cols {
            for d in 0..4 {
                let dr = dirs[d][0];
                let dc = dirs[d][1];
                for _ in 0..steps {
                    r += dr;
                    c += dc;
                    if r >= 0 && r < rows && c >= 0 && c < cols {
                        ans.push(vec![r, c]);
                        if (ans.len() as i32) == rows * cols {
                            return ans;
                        }
                    }
                }
                if d % 2 == 1 {
                    steps += 1;
                }
            }
        }
        ans
    }
}
