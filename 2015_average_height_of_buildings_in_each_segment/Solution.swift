// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

class Solution {
    func averageHeightOfBuildings(_ buildings: [[Int]]) -> [[Int]] {
        var events = [[Int]]()
        for b in buildings {
            events.append([b[0], 1, b[2]])
            events.append([b[1], -1, b[2]])
        }
        events.sort {
            if $0[0] != $1[0] { return $0[0] < $1[0] }
            return $0[1] < $1[1]
        }
        var ans = [[Int]]()
        var count = 0, sum = 0, prev = events[0][0]
        for e in events {
            if e[0] != prev && count > 0 {
                let avg = sum / count
                if let last = ans.last, last[1] == prev && last[2] == avg {
                    ans[ans.count - 1][1] = e[0]
                } else {
                    ans.append([prev, e[0], avg])
                }
            }
            count += e[1]
            sum += e[1] * e[2]
            prev = e[0]
        }
        return ans
    }
}
