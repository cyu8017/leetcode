// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        let mut vals = Vec::new();
        let base = grid[0][0] % x;
        for row in &grid {
            for &v in row {
                if v % x != base {
                    return -1;
                }
                vals.push(v);
            }
        }
        vals.sort_unstable();
        let median = vals[vals.len() / 2];
        let mut ans = 0;
        for v in vals {
            ans += (v - median).abs() / x;
        }
        ans
    }
}
