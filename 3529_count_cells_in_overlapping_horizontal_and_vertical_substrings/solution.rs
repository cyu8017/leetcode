// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

impl Solution {
    pub fn count_cells(grid: Vec<Vec<char>>, pattern: String) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut row = Vec::with_capacity(m * n);
        let mut col = Vec::with_capacity(m * n);
        for i in 0..m {
            for j in 0..n {
                row.push(grid[i][j]);
            }
        }
        for j in 0..n {
            for i in 0..m {
                col.push(grid[i][j]);
            }
        }
        let pat: Vec<char> = pattern.chars().collect();
        let plen = pat.len();
        let mut h_mark = vec![vec![false; n]; m];
        let mut v_mark = vec![vec![false; n]; m];
        if plen > 0 {
            for i in 0..=row.len().saturating_sub(plen) {
                if row[i..i + plen] == pat[..] {
                    for t in 0..plen {
                        let pos = i + t;
                        h_mark[pos / n][pos % n] = true;
                    }
                }
            }
            for i in 0..=col.len().saturating_sub(plen) {
                if col[i..i + plen] == pat[..] {
                    for t in 0..plen {
                        let pos = i + t;
                        v_mark[pos % m][pos / m] = true;
                    }
                }
            }
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                if h_mark[i][j] && v_mark[i][j] {
                    ans += 1;
                }
            }
        }
        ans
    }
}
