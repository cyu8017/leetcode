// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution {
    func findDegrees(_ matrix: [[Int]]) -> [Int] {
        var ans = [Int](repeating: 0, count: matrix.count)
        for i in 0..<matrix.count {
            for x in matrix[i] { ans[i] += x }
        }
        return ans
    }
}
