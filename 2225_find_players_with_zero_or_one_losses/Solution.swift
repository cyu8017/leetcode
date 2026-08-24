// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution {
    func findWinners(_ matches: [[Int]]) -> [[Int]] {
        var lose: [Int: Int] = [:]
        var seen = Set<Int>()
        for m in matches {
            seen.insert(m[0])
            seen.insert(m[1])
            lose[m[1], default: 0] += 1
        }
        var zero: [Int] = []
        var one: [Int] = []
        for p in seen {
            let L = lose[p, default: 0]
            if L == 0 { zero.append(p) }
            else if L == 1 { one.append(p) }
        }
        return [zero.sorted(), one.sorted()]
    }
}
