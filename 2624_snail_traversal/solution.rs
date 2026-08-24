// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

impl Solution {
    pub fn snail(nums: Vec<i32>, rows_count: i32, cols_count: i32) -> Vec<Vec<i32>> {
        if rows_count * cols_count != nums.len() as i32 {
            return vec![];
        }
        let rows = rows_count as usize;
        let cols = cols_count as usize;
        let mut ans = vec![vec![0; cols]; rows];
        let mut idx = 0;
        for c in 0..cols {
            if c % 2 == 0 {
                for r in 0..rows {
                    ans[r][c] = nums[idx];
                    idx += 1;
                }
            } else {
                for r in (0..rows).rev() {
                    ans[r][c] = nums[idx];
                    idx += 1;
                }
            }
        }
        ans
    }
}
