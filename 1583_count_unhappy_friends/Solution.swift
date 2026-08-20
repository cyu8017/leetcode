// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

class Solution {
    func unhappyFriends(_ n: Int, _ preferences: [[Int]], _ pairs: [[Int]]) -> Int {
        var rank = Array(repeating: Array(repeating: 0, count: n), count: n)
        for (i, pref) in preferences.enumerated() {
            for (r, friend) in pref.enumerated() { rank[i][friend] = r }
        }
        var partner = Array(repeating: 0, count: n)
        for p in pairs {
            partner[p[0]] = p[1]
            partner[p[1]] = p[0]
        }
        var unhappy = 0
        for x in 0..<n {
            let y = partner[x]
            for u in preferences[x] {
                if u == y { break }
                if rank[u][x] < rank[u][partner[u]] {
                    unhappy += 1
                    break
                }
            }
        }
        return unhappy
    }
}
