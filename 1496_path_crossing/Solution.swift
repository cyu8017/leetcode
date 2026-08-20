// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

class Solution {
    func isPathCrossing(_ path: String) -> Bool {
        var x = 0, y = 0
        var seen: Set<[Int]> = [[0, 0]]
        let move: [Character: (Int, Int)] = ["N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)]
        for c in path {
            let d = move[c]!
            x += d.0; y += d.1
            if seen.contains([x, y]) { return true }
            seen.insert([x, y])
        }
        return false
    }
}
