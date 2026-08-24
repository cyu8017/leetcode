// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

class Solution {
    var p = [Int]()
    func find(_ x: Int) -> Int {
        if p[x] == x { return x }
        p[x] = find(p[x])
        return p[x]
    }

    func minCost(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        p = Array(0..<n)
        if k == n { return 0 }
        let edges = edges.sorted { $0[2] < $1[2] }
        var cnt = n
        for e in edges {
            let pu = find(e[0]), pv = find(e[1])
            if pu != pv {
                p[pu] = pv
                cnt -= 1
                if cnt <= k { return e[2] }
            }
        }
        return 0
    }
}
