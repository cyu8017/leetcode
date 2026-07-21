// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution {
    func findTheWinner(_ n: Int, _ k: Int) -> Int {
        var pos = 0
        if n >= 2 {
            for size in 2...n {
                pos = (pos + k) % size
            }
        }
        return pos + 1
    }
}
