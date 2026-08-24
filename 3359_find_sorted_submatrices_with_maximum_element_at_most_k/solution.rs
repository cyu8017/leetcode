// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

impl Solution {
    pub fn count_sorted_matrices(grid: Vec<Vec<i32>>, k: i32) -> i64 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0i64;
        for r1 in 0..m {
            for r2 in r1..m {
                for c1 in 0..n {
                    for c2 in c1..n {
                        let mut ok = true;
                        'outer: for i in r1..=r2 {
                            for j in c1..=c2 {
                                if grid[i][j] > k {
                                    ok = false;
                                    break 'outer;
                                }
                                if j > c1 && grid[i][j] < grid[i][j - 1] {
                                    ok = false;
                                    break 'outer;
                                }
                                if i > r1 && grid[i][j] < grid[i - 1][j] {
                                    ok = false;
                                    break 'outer;
                                }
                            }
                        }
                        if ok {
                            ans += 1;
                        }
                    }
                }
            }
        }
        ans
    }
}
