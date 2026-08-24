// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

class Solution {
    func longestSpecialPath(_ edges: [[Int]], _ nums: [Int]) -> [Int] {
        let n = nums.count
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        var bestLen = 0, bestNodes = 1
        func dfs(_ u: Int, _ p: Int, _ dist: Int, _ pathVals: inout [Int], _ pathDist: inout [Int]) {
            pathVals.append(nums[u])
            pathDist.append(dist)
            var freq = [Int: Int]()
            var dups = 0, left = 0
            for right in 0..<pathVals.count {
                let v = pathVals[right]
                freq[v, default: 0] += 1
                if freq[v] == 2 { dups += 1 }
                while dups > 1 {
                    let lv = pathVals[left]
                    if freq[lv] == 2 { dups -= 1 }
                    freq[lv]! -= 1
                    left += 1
                }
            }
            let length = dist - pathDist[left]
            let nodes = pathVals.count - left
            if length > bestLen || (length == bestLen && nodes < bestNodes) {
                bestLen = length
                bestNodes = nodes
            }
            for (v, w) in g[u] where v != p {
                dfs(v, u, dist + w, &pathVals, &pathDist)
            }
            pathVals.removeLast()
            pathDist.removeLast()
        }
        var pv = [Int](), pd = [Int]()
        dfs(0, -1, 0, &pv, &pd)
        return [bestLen, bestNodes]
    }
}
