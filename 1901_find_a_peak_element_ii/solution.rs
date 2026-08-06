// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

impl Solution {
    pub fn find_peak_grid(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let rows = mat.len();
        let cols = mat[0].len();
        let mut lo = 0i32;
        let mut hi = (cols - 1) as i32;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            let mid_usize = mid as usize;
            let mut max_row = 0;
            for r in 1..rows {
                if mat[r][mid_usize] > mat[max_row][mid_usize] {
                    max_row = r;
                }
            }
            let left = if mid > 0 {
                mat[max_row][mid_usize - 1]
            } else {
                -1
            };
            let right = if mid_usize + 1 < cols {
                mat[max_row][mid_usize + 1]
            } else {
                -1
            };
            let cur = mat[max_row][mid_usize];
            if cur >= left && cur >= right {
                return vec![max_row as i32, mid];
            }
            if left > cur {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        vec![0, 0]
    }
}
