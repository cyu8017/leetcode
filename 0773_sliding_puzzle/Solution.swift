// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

class Solution {
    func slidingPuzzle(_ board: [[Int]]) -> Int {
        let start = board.flatMap { $0 }.map(String.init).joined()
        let target = "123450"
        let neighbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        var queue = [start]
        var stepsQ = [0]
        var seen = Set([start])
        var idx = 0
        while idx < queue.count {
            let state = queue[idx]
            let steps = stepsQ[idx]
            idx += 1
            if state == target { return steps }
            let zero = state.firstIndex(of: "0")!
            let z = state.distance(from: state.startIndex, to: zero)
            var chars = Array(state)
            for nei in neighbors[z] {
                chars.swapAt(z, nei)
                let ns = String(chars)
                if seen.insert(ns).inserted {
                    queue.append(ns)
                    stepsQ.append(steps + 1)
                }
                chars.swapAt(z, nei)
            }
        }
        return -1
    }
}
