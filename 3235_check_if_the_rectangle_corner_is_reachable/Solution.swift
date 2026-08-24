// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

class Solution {
    private var xCorner = 0, yCorner = 0
    private var circles: [[Int]] = []
    private var vis: [Bool] = []
    private var n = 0

    func canReachCorner(_ xCorner: Int, _ yCorner: Int, _ circles: [[Int]]) -> Bool {
        self.xCorner = xCorner
        self.yCorner = yCorner
        self.circles = circles
        n = circles.count
        vis = Array(repeating: false, count: n)
        for i in 0..<n {
            let x = circles[i][0], y = circles[i][1], r = circles[i][2]
            if inCircle(0, 0, x, y, r) || inCircle(xCorner, yCorner, x, y, r) { return false }
            if !vis[i] && crossLeftTop(x, y, r) && dfs(i) { return false }
        }
        return true
    }

    private func inCircle(_ x: Int, _ y: Int, _ cx: Int, _ cy: Int, _ r: Int) -> Bool {
        let dx = x - cx, dy = y - cy
        return dx * dx + dy * dy <= r * r
    }

    private func crossLeftTop(_ cx: Int, _ cy: Int, _ r: Int) -> Bool {
        let a = abs(cx) <= r && cy >= 0 && cy <= yCorner
        let b = abs(cy - yCorner) <= r && cx >= 0 && cx <= xCorner
        return a || b
    }

    private func crossRightBottom(_ cx: Int, _ cy: Int, _ r: Int) -> Bool {
        let a = abs(cx - xCorner) <= r && cy >= 0 && cy <= yCorner
        let b = abs(cy) <= r && cx >= 0 && cx <= xCorner
        return a || b
    }

    private func dfs(_ i: Int) -> Bool {
        let x1 = circles[i][0], y1 = circles[i][1], r1 = circles[i][2]
        if crossRightBottom(x1, y1, r1) { return true }
        vis[i] = true
        for j in 0..<n {
            if vis[j] { continue }
            let x2 = circles[j][0], y2 = circles[j][1], r2 = circles[j][2]
            if (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) > (r1 + r2) * (r1 + r2) { continue }
            if x1 * r2 + x2 * r1 < (r1 + r2) * xCorner
                && y1 * r2 + y2 * r1 < (r1 + r2) * yCorner
                && dfs(j) {
                return true
            }
        }
        return false
    }
}
