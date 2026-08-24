// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

class Solution {
    func maximumInvitations(_ favorite: [Int]) -> Int {
        let n = favorite.count
        var indeg = [Int](repeating: 0, count: n)
        var depth = [Int](repeating: 1, count: n)
        for f in favorite { indeg[f] += 1 }
        var q = [Int]()
        for i in 0..<n where indeg[i] == 0 { q.append(i) }
        var head = 0
        while head < q.count {
            let u = q[head]; head += 1
            let v = favorite[u]
            depth[v] = max(depth[v], depth[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0 { q.append(v) }
        }
        var pairSum = 0, maxCycle = 0
        var vis = [Bool](repeating: false, count: n)
        for i in 0..<n {
            if indeg[i] == 0 || vis[i] { continue }
            var u = i, lenCycle = 0
            while !vis[u] {
                vis[u] = true
                u = favorite[u]
                lenCycle += 1
            }
            if lenCycle == 2 { pairSum += depth[i] + depth[favorite[i]] }
            else { maxCycle = max(maxCycle, lenCycle) }
        }
        return max(pairSum, maxCycle)
    }
}
