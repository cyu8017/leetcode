// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

class Solution {

    fun minimumHealth(damage: IntArray, armor: Int): Long {

            var sum = 0
            var mx = 0
            for (d in damage) { sum += d; mx = maxOf(mx, d); }
            return sum - minOf(armor, mx) + 1

    }

}
