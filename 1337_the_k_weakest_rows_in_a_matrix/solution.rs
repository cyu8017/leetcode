// LeetCode 1337 - The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

impl Solution {
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut idx: Vec<usize> = (0..mat.len()).collect();
        idx.sort_by_key(|&i| (mat[i].iter().sum::<i32>(), i));
        idx.into_iter().take(k as usize).map(|i| i as i32).collect()
    }
}
