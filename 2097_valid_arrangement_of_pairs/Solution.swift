// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

class Solution {
    func validArrangement(_ pairs: [[Int]]) -> [[Int]] {
        var g = [Int: [Int]]()
        var indeg = [Int: Int]()
        var outdeg = [Int: Int]()
        for p in pairs {
            g[p[0], default: []].append(p[1])
            outdeg[p[0], default: 0] += 1
            indeg[p[1], default: 0] += 1
        }
        var start = pairs[0][0]
        for (u, o) in outdeg where o - indeg[u, default: 0] == 1 {
            start = u
            break
        }
        var path = [Int]()
        func dfs(_ u: Int) {
            while var nbrs = g[u], !nbrs.isEmpty {
                let v = nbrs.removeLast()
                g[u] = nbrs
                dfs(v)
            }
            path.append(u)
        }
        dfs(start)
        path.reverse()
        var ans = [[Int]]()
        for i in 0..<(path.count - 1) {
            ans.append([path[i], path[i + 1]])
        }
        return ans
    }
}
