// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

class Solution {
    func findCenter(_ edges: [[Int]]) -> Int {
        let (a, b) = (edges[0][0], edges[0][1])
        let (c, d) = (edges[1][0], edges[1][1])
        return (a == c || a == d) ? a : b
    }
}
