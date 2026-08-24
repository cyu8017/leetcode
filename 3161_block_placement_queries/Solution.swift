// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

private class FenwickMax {
    var vals: [Int]
    init(_ n: Int) { vals = Array(repeating: 0, count: n + 1) }
    func maximize(_ i: Int, _ val: Int) {
        var x = i
        while x < vals.count {
            vals[x] = max(vals[x], val)
            x += x & -x
        }
    }
    func get(_ i: Int) -> Int {
        var x = i, res = 0
        while x > 0 {
            res = max(res, vals[x])
            x -= x & -x
        }
        return res
    }
}

class Solution {
    func getResults(_ queries: [[Int]]) -> [Bool] {
        var n = queries.count * 3
        if n > 50000 { n = 50000 }
        let tree = FenwickMax(n + 1)
        var obs = [0, n]
        for q in queries where q[0] == 1 {
            let x = q[1]
            let idx = lowerBound(obs, x)
            if idx == obs.count || obs[idx] != x { obs.insert(x, at: idx) }
        }
        for i in 0..<(obs.count - 1) {
            tree.maximize(obs[i + 1], obs[i + 1] - obs[i])
        }
        var ans: [Bool] = []
        for i in stride(from: queries.count - 1, through: 0, by: -1) {
            let typ = queries[i][0], x = queries[i][1]
            if typ == 1 {
                let j = lowerBound(obs, x)
                let prev = obs[j - 1], next = obs[j + 1]
                obs.remove(at: j)
                tree.maximize(next, next - prev)
            } else {
                let sz = queries[i][2]
                let j = lowerBound(obs, x + 1) - 1
                let prev = obs[j]
                ans.append(tree.get(prev) >= sz || x - prev >= sz)
            }
        }
        return ans.reversed()
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
