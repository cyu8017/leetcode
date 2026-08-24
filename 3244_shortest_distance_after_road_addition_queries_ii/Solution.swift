// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

class Solution {
    func shortestDistanceAfterQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var nxt = Array(1..<n)
        var cnt = n - 1
        return queries.map { q in
            let u = q[0], v = q[1]
            if nxt[u] > 0 && nxt[u] < v {
                var i = nxt[u]
                while i < v {
                    cnt -= 1
                    let ni = nxt[i]
                    nxt[i] = 0
                    i = ni
                }
                nxt[u] = v
            }
            return cnt
        }
    }
}
