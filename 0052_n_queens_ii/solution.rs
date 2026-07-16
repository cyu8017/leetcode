// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

use std::collections::HashSet;

impl Solution {
    pub fn total_n_queens(n: i32) -> i32 {
        let n = n as usize;
        let mut count = 0;
        let mut cols = HashSet::new();
        let mut diag1 = HashSet::new();
        let mut diag2 = HashSet::new();

        fn backtrack(
            row: usize,
            n: usize,
            cols: &mut HashSet<usize>,
            diag1: &mut HashSet<usize>,
            diag2: &mut HashSet<isize>,
            count: &mut i32,
        ) {
            if row == n {
                *count += 1;
                return;
            }

            for col in 0..n {
                if cols.contains(&col)
                    || diag1.contains(&(row + col))
                    || diag2.contains(&((row as isize) - (col as isize)))
                {
                    continue;
                }

                cols.insert(col);
                diag1.insert(row + col);
                diag2.insert((row as isize) - (col as isize));
                backtrack(row + 1, n, cols, diag1, diag2, count);
                cols.remove(&col);
                diag1.remove(&(row + col));
                diag2.remove(&((row as isize) - (col as isize)));
            }
        }

        backtrack(0, n, &mut cols, &mut diag1, &mut diag2, &mut count);
        count
    }
}
