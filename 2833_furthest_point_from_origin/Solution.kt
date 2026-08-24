// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

class Solution {
    fun furthestDistanceFromOrigin(moves: String): Int {
        var L = 0
        var R = 0
        var u = 0
        for (i in 0 until moves.length) {
            var c = moves[i]
            if (c == 'L') L++
            else if (c == 'R') R++
            else u++
        }
        return kotlin.math.abs(L - R) + u
    }
}
