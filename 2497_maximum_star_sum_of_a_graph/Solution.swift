// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

class Solution {
    func maxStarSum(_ vals: [Int], _ edges: [[Int]], _ k: Int) -> Int {
        let n = vals.count
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var ans = vals[0]
        for i in 0..<n {
            var neigh = g[i].map { vals[$0] }.filter { $0 > 0 }.sorted(by: >)
            var sum = vals[i]
            for j in 0..<min(neigh.count, k) { sum += neigh[j] }
            ans = max(ans, sum)
        }
        return ans
    }
}
