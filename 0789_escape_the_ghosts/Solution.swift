// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

class Solution {
    func escapeGhosts(_ ghosts: [[Int]], _ target: [Int]) -> Bool {
        let targetDist = abs(target[0]) + abs(target[1])
        for ghost in ghosts {
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= targetDist {
                return false
            }
        }
        return true
    }
}
