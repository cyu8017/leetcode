// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

class Solution {
    func numberOfCleanRooms(_ room: [[Int]]) -> Int {
        let m = room.count, n = room[0].count
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        var vis = Set<Int>()
        var cleaned = Set<Int>([0])
        var r = 0, c = 0, d = 0
        while vis.insert(r * 10000 + c * 10 + d).inserted {
            let nr = r + dirs[d].0, nc = c + dirs[d].1
            if nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] == 0 {
                r = nr; c = nc
                cleaned.insert(r * 10000 + c)
            } else {
                d = (d + 1) % 4
            }
        }
        return cleaned.count
    }
}
