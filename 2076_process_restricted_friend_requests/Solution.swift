// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

class Solution {
    func friendRequests(_ n: Int, _ restrictions: [[Int]], _ requests: [[Int]]) -> [Bool] {
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        var ans = [Bool](repeating: false, count: requests.count)
        for i in 0..<requests.count {
            let u = find(requests[i][0]), v = find(requests[i][1])
            var ok = true
            if u != v {
                for r in restrictions {
                    let x = find(r[0]), y = find(r[1])
                    if (x == u && y == v) || (x == v && y == u) { ok = false; break }
                }
            }
            ans[i] = ok
            if ok && u != v { parent[u] = v }
        }
        return ans
    }
}
