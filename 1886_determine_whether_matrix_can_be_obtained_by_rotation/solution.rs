// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

impl Solution {
    pub fn find_rotation(mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        let mut current = mat;
        for _ in 0..4 {
            if current == target {
                return true;
            }
            let n = current.len();
            current = (0..n)
                .map(|col| (0..n).map(|row| current[n - 1 - row][col]).collect())
                .collect();
        }
        false
    }
}
