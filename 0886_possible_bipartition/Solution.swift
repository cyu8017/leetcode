// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

class Solution {
    func possibleBipartition(_ n: Int, _ dislikes: [[Int]]) -> Bool {
        var graph = Array(repeating: [Int](), count: n + 1)
        for e in dislikes {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        var color = [Int: Int]()
        for start in 1...n {
            if color[start] != nil { continue }
            var queue = [start]
            color[start] = 0
            var qi = 0
            while qi < queue.count {
                let node = queue[qi]
                qi += 1
                for nei in graph[node] {
                    if color[nei] == nil {
                        color[nei] = color[node]! ^ 1
                        queue.append(nei)
                    } else if color[nei] == color[node] {
                        return false
                    }
                }
            }
        }
        return true
    }
}
