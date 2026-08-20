// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution {
    func findSmallestSetOfVertices(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var incoming = Set<Int>()
        for e in edges { incoming.insert(e[1]) }
        return (0..<n).filter { !incoming.contains($0) }
    }
}
