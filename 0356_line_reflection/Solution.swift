// LeetCode 0356 - Line Reflection
// https://leetcode.com/problems/line-reflection/

class Solution {
    func isReflected(_ points: [[Int]]) -> Bool {
        var pointSet: Set<String> = []
        var minX = Int.max
        var maxX = Int.min

        for point in points {
            let x = point[0]
            let y = point[1]
            pointSet.insert("\(x),\(y)")
            minX = min(minX, x)
            maxX = max(maxX, x)
        }

        let target = minX + maxX
        for point in points {
            let x = point[0]
            let y = point[1]
            if !pointSet.contains("\(target - x),\(y)") {
                return false
            }
        }

        return true
    }
}
