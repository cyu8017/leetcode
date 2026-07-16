// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

class Solution {
    func canWin(_ currentState: String) -> Bool {
        var memo: [String: Bool] = [:]

        func canWinState(_ state: String) -> Bool {
            if let cached = memo[state] {
                return cached
            }
            let chars = Array(state)
            for index in 0..<(chars.count - 1) {
                if chars[index] == "+" && chars[index + 1] == "+" {
                    var next = chars
                    next[index] = "-"
                    next[index + 1] = "-"
                    if !canWinState(String(next)) {
                        memo[state] = true
                        return true
                    }
                }
            }
            memo[state] = false
            return false
        }

        return canWinState(currentState)
    }
}
