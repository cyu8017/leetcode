// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

class Solution {
    func minMoves(_ rooks: [[Int]]) -> Int {
        var r = rooks
        var ans = 0
        r.sort { $0[0] < $1[0] }
        for i in 0..<r.count { ans += abs(r[i][0] - i) }
        r.sort { $0[1] < $1[1] }
        for j in 0..<r.count { ans += abs(r[j][1] - j) }
        return ans
    }
}
