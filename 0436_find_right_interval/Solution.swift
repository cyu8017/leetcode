// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

class Solution {
    func findRightInterval(_ intervals: [[Int]]) -> [Int] {
        let indexed = intervals.enumerated()
            .map { ($0.element[0], $0.offset) }
            .sorted { $0.0 < $1.0 }
        let starts = indexed.map { $0.0 }

        return intervals.map { interval in
            let end = interval[1]
            let position = lowerBound(starts, end)
            return position == starts.count ? -1 : indexed[position].1
        }
    }

    private func lowerBound(_ values: [Int], _ target: Int) -> Int {
        var left = 0
        var right = values.count
        while left < right {
            let mid = left + (right - left) / 2
            if values[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
