// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut memo = vec![vec![vec![i32::MIN; n]; n]; n];
        Self::dp(0, 0, 0, n, &grid, &mut memo).max(0)
    }

    fn dp(
        r1: usize,
        c1: usize,
        c2: usize,
        n: usize,
        grid: &[Vec<i32>],
        memo: &mut [Vec<Vec<i32>>],
    ) -> i32 {
        let r2 = r1 + c1 - c2;
        if r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] == -1 || grid[r2][c2] == -1 {
            return -1_000_000_000;
        }
        if r1 == n - 1 && c1 == n - 1 {
            return grid[r1][c1];
        }
        if memo[r1][c1][c2] != i32::MIN {
            return memo[r1][c1][c2];
        }
        let mut cherries = grid[r1][c1];
        if r1 != r2 || c1 != c2 {
            cherries += grid[r2][c2];
        }
        cherries += Self::dp(r1 + 1, c1, c2, n, grid, memo)
            .max(Self::dp(r1, c1 + 1, c2, n, grid, memo))
            .max(Self::dp(r1 + 1, c1, c2 + 1, n, grid, memo))
            .max(Self::dp(r1, c1 + 1, c2 + 1, n, grid, memo));
        memo[r1][c1][c2] = cherries;
        cherries
    }
}
