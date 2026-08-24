// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

impl Solution {
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        if original.len() as i32 != m * n {
            return vec![];
        }
        let m = m as usize;
        let n = n as usize;
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                ans[i][j] = original[i * n + j];
            }
        }
        ans
    }
}
