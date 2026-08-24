// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

class Solution {
    private var parent = [Int]()
    private var size = [Int]()
    private var parity = [Int]()

    private func find(_ x: Int) -> (Int, Int) {
        if parent[x] == x { return (x, 0) }
        let res = find(parent[x])
        parity[x] ^= res.1
        parent[x] = res.0
        return (res.0, parity[x])
    }

    func countValidEdges(_ n: Int, _ edges: [[Int]]) -> Int {
        parent = Array(0..<n)
        size = [Int](repeating: 1, count: n)
        parity = [Int](repeating: 0, count: n)
        var ans = 0
        for e in edges {
            var fu = find(e[0])
            var fv = find(e[1])
            var ru = fu.0, pu = fu.1, rv = fv.0, pv = fv.1
            if ru == rv {
                if (pu ^ pv) == e[2] { ans += 1 }
                continue
            }
            if size[ru] < size[rv] {
                swap(&ru, &rv)
                swap(&pu, &pv)
            }
            parent[rv] = ru
            parity[rv] = pu ^ pv ^ e[2]
            size[ru] += size[rv]
            ans += 1
        }
        return ans
    }
}
