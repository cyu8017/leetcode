// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

class Solution {
    func validSquare(_ p1: [Int], _ p2: [Int], _ p3: [Int], _ p4: [Int]) -> Bool {
        let points = [p1, p2, p3, p4]
        var distances = [Int]()
        for i in 0..<4 {
            for j in (i + 1)..<4 {
                let dx = points[i][0] - points[j][0]
                let dy = points[i][1] - points[j][1]
                distances.append(dx * dx + dy * dy)
            }
        }
        distances.sort()
        return distances[0] > 0 && distances[0] == distances[1] && distances[1] == distances[2]
            && distances[2] == distances[3] && distances[4] == distances[5]
            && distances[4] == 2 * distances[0]
    }
}
