// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

protocol Sea {
    func hasShips(_ topRight: [Int], _ bottomLeft: [Int]) -> Bool
}

class Solution {
    func countShips(_ sea: Sea, _ topRight: [Int], _ bottomLeft: [Int]) -> Int {
        let x1 = bottomLeft[0], y1 = bottomLeft[1]
        let x2 = topRight[0], y2 = topRight[1]
        if x1 > x2 || y1 > y2 { return 0 }
        if !sea.hasShips(topRight, bottomLeft) { return 0 }
        if x1 == x2 && y1 == y2 { return 1 }
        let mx = (x1 + x2) / 2, my = (y1 + y2) / 2
        return countShips(sea, [mx, my], [x1, y1])
            + countShips(sea, [mx, y2], [x1, my + 1])
            + countShips(sea, [x2, my], [mx + 1, y1])
            + countShips(sea, [x2, y2], [mx + 1, my + 1])
    }
}
