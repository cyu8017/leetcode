// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

impl Solution {
    pub fn find_center(edges: Vec<Vec<i32>>) -> i32 {
        let (a, b) = (edges[0][0], edges[0][1]);
        let (c, d) = (edges[1][0], edges[1][1]);
        if a == c || a == d { a } else { b }
    }
}
