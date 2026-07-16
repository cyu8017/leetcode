// LeetCode 0352 - Data Stream as Disjoint Intervals
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

class SummaryRanges {
    private var intervals: [[Int]] = []

    init() {
    }

    func addNum(_ value: Int) {
        var newInterval = [value, value]
        var merged: [[Int]] = []
        var inserted = false

        for interval in intervals {
            if interval[1] < value - 1 {
                merged.append(interval)
            } else if interval[0] > value + 1 {
                if !inserted {
                    merged.append(newInterval)
                    inserted = true
                }
                merged.append(interval)
            } else {
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            }
        }

        if !inserted {
            merged.append(newInterval)
        }

        intervals = merged
    }

    func getIntervals() -> [[Int]] {
        intervals
    }
}
