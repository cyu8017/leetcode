// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

class Solution {
    func flipgame(_ fronts: [Int], _ backs: [Int]) -> Int {
        var same = Set<Int>()
        for i in 0..<fronts.count where fronts[i] == backs[i] { same.insert(fronts[i]) }
        var best = Int.max
        for x in fronts where !same.contains(x) { best = min(best, x) }
        for x in backs where !same.contains(x) { best = min(best, x) }
        return best == Int.max ? 0 : best
    }
}
