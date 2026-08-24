// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

class Solution {
    func calc(_ left: Int, _ right: Int, _ isCycle: Bool) -> Int {
        var w0 = right, w1 = right
        var score = 0
        if right - 1 >= left {
            for value in stride(from: right - 1, through: left, by: -1) {
                score += w0 * value
                w0 = w1
                w1 = value
            }
        }
        if isCycle { score += w0 * w1 }
        return score
    }

    func maxScore(_ n: Int, _ edges: [[Int]]) -> Int {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        var seen = Array(repeating: false, count: n)
        var cycleSizes = [Int]()
        var pathSizes = [Int]()
        for i in 0..<n {
            if seen[i] { continue }
            let comp = getComp(i, graph, &seen)
            var allDeg2 = true
            for u in comp where graph[u].count != 2 { allDeg2 = false; break }
            if allDeg2 { cycleSizes.append(comp.count) }
            else if comp.count > 1 { pathSizes.append(comp.count) }
        }
        var ans = 0
        var curN = n
        for cs in cycleSizes {
            ans += calc(curN - cs + 1, curN, true)
            curN -= cs
        }
        pathSizes.sort(by: >)
        for ps in pathSizes {
            ans += calc(curN - ps + 1, curN, false)
            curN -= ps
        }
        return ans
    }

    func getComp(_ start: Int, _ graph: [[Int]], _ seen: inout [Bool]) -> [Int] {
        var comp = [start]
        seen[start] = true
        var i = 0
        while i < comp.count {
            for v in graph[comp[i]] {
                if !seen[v] { seen[v] = true; comp.append(v) }
            }
            i += 1
        }
        return comp
    }
}
