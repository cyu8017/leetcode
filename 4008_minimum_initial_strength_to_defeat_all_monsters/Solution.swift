// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/


class Solution {
    func minInitialStrength(_ monsters: [Int], _ boosts: [[Int]]) -> Int {
        let n = monsters.count
        var d = Array(repeating: 0, count: n + 1)
        for b in boosts {
            d[b[0]] += b[2]
            d[b[1] + 1] -= b[2]
        }
        func check(_ v0: Int) -> Bool {
            var v = v0, bonus = 0
            for i in 0..<monsters.count {
                bonus += d[i]
                if v + bonus < monsters[i] { return false }
                v -= monsters[i]
                if v < 0 { v = 0 }
            }
            return true
        }
        var left = 0, right = 1_000_000_000_000_000
        while left < right {
            let mid = (left + right) / 2
            if check(mid) { right = mid }
            else { left = mid + 1 }
        }
        return left
    }
}
