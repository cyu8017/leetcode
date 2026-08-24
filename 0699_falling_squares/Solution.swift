// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

class Solution {
    func fallingSquares(_ positions: [[Int]]) -> [Int] {
        var intervals = [[Int]]()
        var answer = [Int]()
        var maxHeight = 0
        for pos in positions {
            let left = pos[0], side = pos[1], right = left + side
            var bas = 0
            for it in intervals where it[1] > left && it[0] < right {
                bas = max(bas, it[2])
            }
            let height = bas + side
            intervals.append([left, right, height])
            maxHeight = max(maxHeight, height)
            answer.append(maxHeight)
        }
        return answer
    }
}
