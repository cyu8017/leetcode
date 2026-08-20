// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution {
    func earliestAcq(_ logs: [[Int]], _ n: Int) -> Int {
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        func union(_ a: Int, _ b: Int) -> Bool {
            let ra = find(a), rb = find(b)
            if ra == rb { return false }
            parent[rb] = ra
            return true
        }
        var logs = logs.sorted { $0[0] < $1[0] }
        var components = n
        for log in logs {
            if union(log[1], log[2]) {
                components -= 1
                if components == 1 { return log[0] }
            }
        }
        return -1
    }
}
