// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution {
    func nearestValidPoint(_ x: Int, _ y: Int, _ points: [[Int]]) -> Int {
        var best = Int.max
        var ans = -1
        for (i, point) in points.enumerated() {
            let px = point[0]
            let py = point[1]
            if px != x && py != y {
                continue
            }
            let dist = abs(px - x) + abs(py - y)
            if dist < best {
                best = dist
                ans = i
            }
        }
        return ans
    }
}
