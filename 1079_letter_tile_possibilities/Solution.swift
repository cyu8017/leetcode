// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

class Solution {
    func numTilePossibilities(_ tiles: String) -> Int {
        var count: [Character: Int] = [:]
        for ch in tiles {
            count[ch, default: 0] += 1
        }

        func dfs() -> Int {
            var total = 0
            for (ch, freq) in count {
                if freq == 0 { continue }
                count[ch]! -= 1
                total += 1 + dfs()
                count[ch]! += 1
            }
            return total
        }

        return dfs()
    }
}
