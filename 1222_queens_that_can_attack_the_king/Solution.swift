// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution {
    func queensAttacktheKing(_ queens: [[Int]], _ king: [Int]) -> [[Int]] {
        let qset = Set(queens.map { $0[0] * 8 + $0[1] })
        var ans: [[Int]] = []
        let dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        for (dr, dc) in dirs {
            var r = king[0] + dr, c = king[1] + dc
            while r >= 0 && r < 8 && c >= 0 && c < 8 {
                if qset.contains(r * 8 + c) {
                    ans.append([r, c])
                    break
                }
                r += dr; c += dc
            }
        }
        return ans
    }
}
