// LeetCode 3898 - Find the Degree of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

impl Solution {
    pub fn find_degrees(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        matrix.iter().map(|row| row.iter().sum()).collect()
    }
}
