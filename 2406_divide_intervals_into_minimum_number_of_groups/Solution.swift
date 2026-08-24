// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution {
    func minGroups(_ intervals: [[Int]]) -> Int {
        var events: [(Int, Int)] = []
        for it in intervals {
            events.append((it[0], 1))
            events.append((it[1] + 1, -1))
        }
        events.sort {
            if $0.0 != $1.0 { return $0.0 < $1.0 }
            return $0.1 < $1.1
        }
        var cur = 0, ans = 0
        for e in events {
            cur += e.1
            ans = max(ans, cur)
        }
        return ans
    }
}
