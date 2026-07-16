// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

class Solution {
    private var memo: [String: Int] = [:]

    func findMinStep(_ board: String, _ hand: String) -> Int {
        memo = [:]
        let result = dfs(board, hand)
        return result == Int.max ? -1 : result
    }

    private func shrink(_ s: String) -> String {
        let chars = Array(s)
        var index = 0
        while index < chars.count {
            var end = index
            while end < chars.count && chars[end] == chars[index] {
                end += 1
            }
            if end - index >= 3 {
                let prefix = String(chars[0..<index])
                let suffix = end < chars.count ? String(chars[end...]) : ""
                return shrink(prefix + suffix)
            }
            index = end
        }
        return s
    }

    private func dfs(_ board: String, _ hand: String) -> Int {
        let key = board + "|" + hand
        if let cached = memo[key] {
            return cached
        }

        let shrunk = shrink(board)
        if shrunk.isEmpty {
            memo[key] = 0
            return 0
        }

        var best = Int.max
        let boardChars = Array(shrunk)
        let handChars = Array(hand)
        for insert in 0...boardChars.count {
            for pick in 0..<handChars.count {
                let color = handChars[pick]
                if insert < boardChars.count && boardChars[insert] == color {
                    continue
                }
                if insert > 0 && boardChars[insert - 1] == color {
                    continue
                }
                let prefix = String(boardChars[0..<insert])
                let suffix = insert < boardChars.count ? String(boardChars[insert...]) : ""
                let newBoard = shrink(prefix + String(color) + suffix)
                if newBoard == shrunk {
                    continue
                }
                var newHandChars = handChars
                newHandChars.remove(at: pick)
                let newHand = String(newHandChars)
                let steps = dfs(newBoard, newHand)
                if steps != Int.max {
                    best = min(best, steps + 1)
                }
            }
        }
        memo[key] = best
        return best
    }
}
