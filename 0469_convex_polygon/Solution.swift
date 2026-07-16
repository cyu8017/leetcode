// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

class Solution {
    func isConvex(_ points: [[Int]]) -> Bool {
        var direction = 0
        let count = points.count

        for index in 0..<count {
            let x1 = points[(index + 1) % count][0] - points[index][0]
            let y1 = points[(index + 1) % count][1] - points[index][1]
            let x2 = points[(index + 2) % count][0] - points[(index + 1) % count][0]
            let y2 = points[(index + 2) % count][1] - points[(index + 1) % count][1]
            let cross = x1 * y2 - y1 * x2
            if cross == 0 {
                continue
            }

            let current = cross > 0 ? 1 : -1
            if direction != 0 && direction != current {
                return false
            }
            if direction == 0 {
                direction = current
            }
        }

        return true
    }
}
