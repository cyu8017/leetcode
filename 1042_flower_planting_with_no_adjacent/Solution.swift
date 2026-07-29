// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

class Solution {
    func gardenNoAdj(_ n: Int, _ paths: [[Int]]) -> [Int] {
        var graph = Array(repeating: [Int](), count: n + 1)
        for p in paths {
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])
        }
        var ans = Array(repeating: 0, count: n + 1)
        for garden in 1...n {
            var used = Set<Int>()
            for nei in graph[garden] { used.insert(ans[nei]) }
            for c in 1...4 {
                if !used.contains(c) {
                    ans[garden] = c
                    break
                }
            }
        }
        return Array(ans[1...])
    }
}
