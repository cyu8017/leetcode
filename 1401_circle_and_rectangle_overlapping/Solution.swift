// LeetCode 1401 - Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

class Solution {
    func checkOverlap(_ radius: Int, _ xCenter: Int, _ yCenter: Int, _ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Bool {
        let x = min(max(xCenter, x1), x2)
        let y = min(max(yCenter, y1), y2)
        return (x - xCenter) * (x - xCenter) + (y - yCenter) * (y - yCenter) <= radius * radius
    }
}
