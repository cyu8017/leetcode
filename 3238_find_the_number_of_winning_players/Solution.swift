// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution {
    func winningPlayerCount(_ n: Int, _ pick: [[Int]]) -> Int {
        var cnt = Array(repeating: Array(repeating: 0, count: 11), count: n)
        var s = Set<Int>()
        for p in pick {
            let x = p[0], y = p[1]
            cnt[x][y] += 1
            if cnt[x][y] > x { s.insert(x) }
        }
        return s.count
    }
}
