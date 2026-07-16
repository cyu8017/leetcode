// LeetCode 0223 - Rectangle Area
// https://leetcode.com/problems/rectangle-area/

class Solution {
    func computeArea(_ ax1: Int, _ ay1: Int, _ ax2: Int, _ ay2: Int, _ bx1: Int, _ by1: Int, _ bx2: Int, _ by2: Int) -> Int {
        let areaA = (ax2 - ax1) * (ay2 - ay1)
        let areaB = (bx2 - bx1) * (by2 - by1)
        let overlapW = max(0, min(ax2, bx2) - max(ax1, bx1))
        let overlapH = max(0, min(ay2, by2) - max(ay1, by1))
        return areaA + areaB - overlapW * overlapH
    }
}
