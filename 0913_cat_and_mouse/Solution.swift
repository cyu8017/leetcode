// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

class Solution {
    func catMouseGame(_ graph: [[Int]]) -> Int {
        let n = graph.count
        let mouseWin = 1, catWin = 2
        var states = Array(repeating: Array(repeating: Array(repeating: 0, count: 2), count: n), count: n)
        var outDegree = Array(repeating: Array(repeating: Array(repeating: 0, count: 2), count: n), count: n)
        var q = [(Int, Int, Int, Int)]()
        for cat in 0..<n {
            for mouse in 0..<n {
                outDegree[cat][mouse][0] = graph[mouse].count
                outDegree[cat][mouse][1] = graph[cat].filter { $0 != 0 }.count
            }
        }
        if n > 1 {
            for cat in 1..<n {
                for move in 0..<2 {
                    states[cat][0][move] = mouseWin
                    q.append((cat, 0, move, mouseWin))
                    states[cat][cat][move] = catWin
                    q.append((cat, cat, move, catWin))
                }
            }
        }
        var qi = 0
        while qi < q.count {
            let (cat, mouse, move, state) = q[qi]
            qi += 1
            if cat == 2 && mouse == 1 && move == 0 { return state }
            let prevMove = move ^ 1
            for prev in graph[prevMove == 1 ? cat : mouse] {
                let prevCat = prevMove == 1 ? prev : cat
                if prevCat == 0 { continue }
                let prevMouse = prevMove == 1 ? mouse : prev
                if states[prevCat][prevMouse][prevMove] != 0 { continue }
                if (prevMove == 0 && state == mouseWin) || (prevMove == 1 && state == catWin) || outDegree[prevCat][prevMouse][prevMove] == 1 {
                    states[prevCat][prevMouse][prevMove] = state
                    q.append((prevCat, prevMouse, prevMove, state))
                } else {
                    outDegree[prevCat][prevMouse][prevMove] -= 1
                }
            }
        }
        return states[2][1][0]
    }
}
