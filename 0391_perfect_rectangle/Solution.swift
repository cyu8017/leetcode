// LeetCode 0391 - Perfect Rectangle
// https://leetcode.com/problems/perfect-rectangle/

class Solution {
    func isRectangleCover(_ rectangles: [[Int]]) -> Bool {
        var points: Set<String> = []
        var area = 0
        var minX = Int.max
        var minY = Int.max
        var maxX = Int.min
        var maxY = Int.min

        for rectangle in rectangles {
            let x1 = rectangle[0]
            let y1 = rectangle[1]
            let x2 = rectangle[2]
            let y2 = rectangle[3]
            area += (x2 - x1) * (y2 - y1)
            minX = min(minX, x1)
            minY = min(minY, y1)
            maxX = max(maxX, x2)
            maxY = max(maxY, y2)

            for point in ["\(x1),\(y1)", "\(x1),\(y2)", "\(x2),\(y1)", "\(x2),\(y2)"] {
                if points.contains(point) {
                    points.remove(point)
                } else {
                    points.insert(point)
                }
            }
        }

        let corners: Set<String> = [
            "\(minX),\(minY)",
            "\(minX),\(maxY)",
            "\(maxX),\(minY)",
            "\(maxX),\(maxY)",
        ]
        if points != corners {
            return false
        }

        return area == (maxX - minX) * (maxY - minY)
    }
}
