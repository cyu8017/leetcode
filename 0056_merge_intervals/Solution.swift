// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        let sorted = intervals.sorted { $0[0] < $1[0] }
        var merged = [sorted[0]]

        for current in sorted.dropFirst() {
            var last = merged[merged.count - 1]

            if current[0] <= last[1] {
                last[1] = max(last[1], current[1])
                merged[merged.count - 1] = last
            } else {
                merged.append(current)
            }
        }

        return merged
    }
}
