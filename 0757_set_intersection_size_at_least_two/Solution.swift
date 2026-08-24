// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

class Solution {
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        let intervals = intervals.sorted { a, b in a[1] != b[1] ? a[1] < b[1] : a[0] < b[0] }
        var size = 0, first = -1, second = -1
        for interval in intervals {
            let left = interval[0], right = interval[1]
            if left <= first { continue }
            if left <= second { size += 1; first = second; second = right }
            else { size += 2; first = right - 1; second = right }
        }
        return size
    }
}
