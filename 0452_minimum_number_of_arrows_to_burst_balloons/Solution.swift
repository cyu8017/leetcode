// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution {
    func findMinArrowShots(_ points: [[Int]]) -> Int {
        if points.isEmpty {
            return 0
        }

        let sorted = points.sorted { $0[1] < $1[1] }
        var arrows = 1
        var end = sorted[0][1]

        for index in 1..<sorted.count {
            let start = sorted[index][0]
            let finish = sorted[index][1]
            if start > end {
                arrows += 1
                end = finish
            }
        }

        return arrows
    }
}
