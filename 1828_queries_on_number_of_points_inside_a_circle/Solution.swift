// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution {
    func countPoints(_ points: [[Int]], _ queries: [[Int]]) -> [Int] {
        var result = [Int]()
        for q in queries {
            let xq = q[0], yq = q[1], r = q[2]
            let radiusSq = r * r
            var count = 0
            for p in points {
                let dx = p[0] - xq
                let dy = p[1] - yq
                if dx * dx + dy * dy <= radiusSq { count += 1 }
            }
            result.append(count)
        }
        return result
    }
}
