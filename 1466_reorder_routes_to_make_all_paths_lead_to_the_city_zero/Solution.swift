// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution {
    func minReorder(_ n: Int, _ connections: [[Int]]) -> Int {
        var graph = Array(repeating: [(Int, Int)](), count: n)
        for e in connections {
            graph[e[0]].append((e[1], 1))
            graph[e[1]].append((e[0], 0))
        }
        var ans = 0, stack = [0], seen: Set<Int> = [0]
        while !stack.isEmpty {
            let node = stack.removeLast()
            for (nei, cost) in graph[node] where !seen.contains(nei) {
                seen.insert(nei); stack.append(nei); ans += cost
            }
        }
        return ans
    }
}
