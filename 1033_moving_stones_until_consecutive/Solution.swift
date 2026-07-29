// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

class Solution {
    func numMovesStones(_ a: Int, _ b: Int, _ c: Int) -> [Int] {
        let sorted = [a, b, c].sorted()
        let x = sorted[0], y = sorted[1], z = sorted[2]
        let minMoves: Int
        if z - x == 2 { minMoves = 0 }
        else if y - x <= 2 || z - y <= 2 { minMoves = 1 }
        else { minMoves = 2 }
        return [minMoves, z - x - 2]
    }
}
