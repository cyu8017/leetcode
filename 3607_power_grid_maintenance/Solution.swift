// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

class Solution {
    var parent = [Int]()

    func find(_ x: Int) -> Int {
        if parent[x] != x { parent[x] = find(parent[x]) }
        return parent[x]
    }

    func unite(_ a: Int, _ b: Int) {
        let ra = find(a), rb = find(b)
        if ra != rb {
            if ra < rb { parent[rb] = ra } else { parent[ra] = rb }
        }
    }

    func processQueries(_ c: Int, _ connections: [[Int]], _ queries: [[Int]]) -> [Int] {
        parent = Array(0...c)
        for e in connections { unite(e[0], e[1]) }
        var online = Array(repeating: true, count: c + 1)
        var comp = [Int: [Int]]()
        for i in 1...c { comp[find(i), default: []].append(i) }
        for k in comp.keys { comp[k]!.sort() }
        var ptr = [Int: Int]()
        var ans = [Int]()
        for q in queries {
            let t = q[0], x = q[1]
            if t == 2 { online[x] = false; continue }
            if online[x] { ans.append(x); continue }
            let r = find(x)
            let ids = comp[r]!
            var p = ptr[r] ?? 0
            while p < ids.count && !online[ids[p]] { p += 1 }
            ptr[r] = p
            ans.append(p < ids.count ? ids[p] : -1)
        }
        return ans
    }
}
