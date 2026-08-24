// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

class Solution {
    func flowerGame(_ n: Int, _ m: Int) -> Int {
        let a1 = (n + 1) / 2, b1 = (m + 1) / 2
        let a2 = n / 2, b2 = m / 2
        return a1 * b2 + a2 * b1
    }
}
