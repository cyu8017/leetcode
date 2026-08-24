// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

class Solution {
    var g = [[Int]]()
    var xorPath = [Int]()
    var vals = [Int]()
    var inT = [Int]()
    var outT = [Int]()
    var order = [Int]()

    func dfs(_ u: Int) {
        xorPath[u] ^= vals[u]
        for v in g[u] {
            xorPath[v] = xorPath[u]
            dfs(v)
        }
    }

    func dfs2(_ u: Int) {
        inT[u] = order.count
        order.append(xorPath[u])
        for v in g[u] { dfs2(v) }
        outT[u] = order.count
    }

    func kthSmallest(_ par: [Int], _ vals: [Int], _ queries: [[Int]]) -> [Int] {
        let n = par.count
        self.vals = vals
        g = Array(repeating: [], count: n)
        if n > 1 {
            for i in 1..<n { g[par[i]].append(i) }
        }
        xorPath = Array(repeating: 0, count: n)
        dfs(0)
        inT = Array(repeating: 0, count: n)
        outT = Array(repeating: 0, count: n)
        order = []
        dfs2(0)
        var ans = Array(repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let u = queries[i][0], k = queries[i][1]
            var sub = Array(order[inT[u]..<outT[u]])
            sub.sort()
            var uniq = [Int]()
            for x in sub {
                if uniq.isEmpty || uniq.last! != x { uniq.append(x) }
            }
            ans[i] = k > uniq.count ? -1 : uniq[k - 1]
        }
        return ans
    }
}
