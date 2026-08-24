// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

class Solution {
    fun maxDistance(moves: String): Int {
        var x = 0
        var y = 0
        var z = 0
        for (i in 0 until moves.length) {
            var c = moves[i]
            if (c == 'U') x -= 1
            else if (c == 'D') x += 1
            else if (c == 'L') y -= 1
            else if (c == 'R') y += 1
            else z += 1
        }
        return kotlin.math.abs(x) + kotlin.math.abs(y) + z
    }
}
