// LeetCode 0057 - Insert Interval
// https://leetcode.com/problems/insert-interval/

class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        var result: [[Int]] = []
        var i = 0
        var merged = newInterval

        while i < intervals.count && intervals[i][1] < merged[0] {
            result.append(intervals[i])
            i += 1
        }

        while i < intervals.count && intervals[i][0] <= merged[1] {
            merged[0] = min(merged[0], intervals[i][0])
            merged[1] = max(merged[1], intervals[i][1])
            i += 1
        }

        result.append(merged)

        while i < intervals.count {
            result.append(intervals[i])
            i += 1
        }

        return result
    }
}
