// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

class Solution {
    func longestSpecialPath(_ edges: [[Int]], _ nums: [Int]) -> [Int] {
        let n = nums.count
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        var bestLen = 0, bestNodes = 1
        var last = [Int: Int]()
        var path = [Int]()
        func dfs(_ u: Int, _ p: Int, _ dist: Int, _ left: Int) {
            let seen = last[nums[u]] != nil
            let prevPos = last[nums[u]] ?? -1
            last[nums[u]] = path.count
            var newLeft = left
            if seen && prevPos >= left { newLeft = prevPos + 1 }
            path.append(dist)
            let length = dist - path[newLeft]
            let nodes = path.count - newLeft
            if length > bestLen || (length == bestLen && nodes < bestNodes) {
                bestLen = length
                bestNodes = nodes
            }
            for (v, w) in g[u] where v != p {
                dfs(v, u, dist + w, newLeft)
            }
            path.removeLast()
            if seen { last[nums[u]] = prevPos }
            else { last.removeValue(forKey: nums[u]) }
        }
        dfs(0, -1, 0, 0)
        return [bestLen, bestNodes]
    }
}
