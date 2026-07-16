// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

class Solution {
    func generatePossibleNextMoves(_ currentState: String) -> [String] {
        var result: [String] = []
        let chars = Array(currentState)
        guard chars.count > 1 else {
            return result
        }
        for index in 0..<(chars.count - 1) {
            if chars[index] == "+" && chars[index + 1] == "+" {
                var next = chars
                next[index] = "-"
                next[index + 1] = "-"
                result.append(String(next))
            }
        }
        return result
    }
}
