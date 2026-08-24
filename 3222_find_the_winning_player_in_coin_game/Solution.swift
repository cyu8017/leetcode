// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution {
    func losingPlayer(_ x: Int, _ y: Int) -> String {
        let k = min(x / 2, y / 8)
        let xx = x - 2 * k
        let yy = y - 8 * k
        if xx > 0 && yy >= 4 { return "Alice" }
        return "Bob"
    }
}
