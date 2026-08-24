// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/


class Solution {
    func filterOccupiedIntervals(_ occupiedIntervals: [[Int]], _ freeStart: Int, _ freeEnd: Int) -> [[Int]] {
        var occupied = occupiedIntervals.sorted { $0[0] < $1[0] }
        var busy = [[occupied[0][0], occupied[0][1]]]
        for i in 1..<occupied.count {
            let cur = occupied[i]
            if busy[busy.count - 1][1] + 1 < cur[0] {
                busy.append([cur[0], cur[1]])
            } else if cur[1] > busy[busy.count - 1][1] {
                busy[busy.count - 1][1] = cur[1]
            }
        }
        var ans = [[Int]]()
        for it in busy {
            let s = it[0], e = it[1]
            if e < freeStart || s > freeEnd {
                ans.append([s, e])
            } else {
                if s < freeStart { ans.append([s, freeStart - 1]) }
                if e > freeEnd { ans.append([freeEnd + 1, e]) }
            }
        }
        return ans
    }
}
