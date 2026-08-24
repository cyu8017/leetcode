// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

class Solution {
    func minStickers(_ stickers: [String], _ target: String) -> Int {
        var need = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        func idx(_ ch: Character) -> Int { Int(ch.asciiValue! - a) }
        for ch in target { need[idx(ch)] += 1 }
        var chars = [Character]()
        for i in 0..<26 where need[i] > 0 { chars.append(Character(UnicodeScalar(Int(a) + i)!)) }
        var sticks = [[Int]]()
        for sticker in stickers {
            var counts = Array(repeating: 0, count: 26)
            for ch in sticker { counts[idx(ch)] += 1 }
            if chars.contains(where: { counts[idx($0)] > 0 }) { sticks.append(counts) }
        }
        var memo = [[Int]: Int]()
        func dfs(_ state: [Int]) -> Int {
            if let cached = memo[state] { return cached }
            if let i = state.firstIndex(where: { $0 > 0 }) {
                let first = chars[i]
                var best = Int.max / 4
                for stick in sticks {
                    if stick[idx(first)] == 0 { continue }
                    var nxt = state
                    for j in 0..<chars.count {
                        nxt[j] = max(0, nxt[j] - stick[idx(chars[j])])
                    }
                    best = min(best, 1 + dfs(nxt))
                }
                memo[state] = best
                return best
            }
            memo[state] = 0
            return 0
        }
        var state = chars.map { need[idx($0)] }
        let result = dfs(state)
        return result >= Int.max / 4 ? -1 : result
    }
}
