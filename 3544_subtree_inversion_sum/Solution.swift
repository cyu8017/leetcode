// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

class Solution {
    var graph = [[Int]]()
    var nums = [Int]()
    var parent = [Int]()
    var k = 0
    var memo = [String: Int]()

    func subtreeInversionSum(_ edges: [[Int]], _ nums: [Int], _ k: Int) -> Int {
        let n = edges.count + 1
        self.nums = nums
        self.k = k
        graph = Array(repeating: [], count: n)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        parent = Array(repeating: -1, count: n)
        memo = [:]
        return dp(0, k, false)
    }

    func dp(_ u: Int, _ steps: Int, _ inv: Bool) -> Int {
        let key = "\(u),\(steps),\(inv)"
        if let v = memo[key] { return v }
        var num = nums[u]
        if inv { num = -num }
        var negNum = -num
        for v in graph[u] {
            if v == parent[u] { continue }
            parent[v] = u
            var ns = steps + 1
            if ns > k { ns = k }
            num += dp(v, ns, inv)
            if steps == k { negNum += dp(v, 1, !inv) }
        }
        var res = num
        if steps == k && negNum > res { res = negNum }
        memo[key] = res
        return res
    }
}
