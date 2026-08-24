// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

class Solution {
    func minRunesToAdd(_ n: Int, _ crystals: [Int], _ flowFrom: [Int], _ flowTo: [Int]) -> Int {
        var g = Array(repeating: [Int](), count: n)
        var rg = Array(repeating: [Int](), count: n)
        for i in 0..<flowFrom.count {
            g[flowFrom[i]].append(flowTo[i])
            rg[flowTo[i]].append(flowFrom[i])
        }
        var vis = Array(repeating: false, count: n)
        var order = [Int]()
        func dfs1(_ u: Int) {
            vis[u] = true
            for v in g[u] where !vis[v] { dfs1(v) }
            order.append(u)
        }
        for i in 0..<n where !vis[i] { dfs1(i) }
        var comp = Array(repeating: -1, count: n)
        var cid = 0
        func dfs2(_ u: Int) {
            comp[u] = cid
            for v in rg[u] where comp[v] == -1 { dfs2(v) }
        }
        for u in order.reversed() where comp[u] == -1 {
            dfs2(u)
            cid += 1
        }
        var hasCrystal = Array(repeating: false, count: cid)
        for c in crystals { hasCrystal[comp[c]] = true }
        var indeg = Array(repeating: 0, count: cid)
        for u in 0..<n {
            for v in g[u] where comp[u] != comp[v] { indeg[comp[v]] += 1 }
        }
        var ans = 0
        for i in 0..<cid where indeg[i] == 0 && !hasCrystal[i] { ans += 1 }
        return ans
    }
}
