// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

class Solution {
    func bestTower(_ towers: [[Int]], _ center: [Int], _ radius: Int) -> [Int] {
        let cx = center[0], cy = center[1]
        var idx = -1
        for i in 0..<towers.count {
            let x = towers[i][0], y = towers[i][1], q = towers[i][2]
            let dist = abs(x - cx) + abs(y - cy)
            if dist > radius { continue }
            if idx == -1 || towers[idx][2] < q ||
                (towers[idx][2] == q &&
                 (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1]))) {
                idx = i
            }
        }
        if idx == -1 { return [-1, -1] }
        return [towers[idx][0], towers[idx][1]]
    }
}
