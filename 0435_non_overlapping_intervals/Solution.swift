// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

class Solution {
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        let sorted = intervals.sorted { $0[1] < $1[1] }
        var removed = 0
        var end = Int.min

        for interval in sorted {
            let start = interval[0]
            let finish = interval[1]
            if start < end {
                removed += 1
            } else {
                end = finish
            }
        }

        return removed
    }
}
