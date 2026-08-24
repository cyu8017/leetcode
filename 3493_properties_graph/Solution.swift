// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

class Solution {
    func numberOfComponents(_ properties: [[Int]], _ k: Int) -> Int {
        let n = properties.count
        var sets = properties.map { Set($0) }
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) {
            let ra = find(a), rb = find(b)
            if ra != rb { parent[ra] = rb }
        }
        for i in 0..<n {
            for j in (i + 1)..<n {
                var cnt = 0
                for v in sets[i] where sets[j].contains(v) { cnt += 1 }
                if cnt >= k { unite(i, j) }
            }
        }
        return Set((0..<n).map { find($0) }).count
    }
}
