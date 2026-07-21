// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution {
    fun findTheWinner(n: Int, k: Int): Int {
        var pos = 0
        for (size in 2..n) {
            pos = (pos + k) % size
        }
        return pos + 1
    }
}
