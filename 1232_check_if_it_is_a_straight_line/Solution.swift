// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution {
    func checkStraightLine(_ coordinates: [[Int]]) -> Bool {
        let dx = coordinates[1][0] - coordinates[0][0]
        let dy = coordinates[1][1] - coordinates[0][1]
        for i in 2..<coordinates.count {
            let x = coordinates[i][0] - coordinates[0][0]
            let y = coordinates[i][1] - coordinates[0][1]
            if dx * y != dy * x { return false }
        }
        return true
    }
}
