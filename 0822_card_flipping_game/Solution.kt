// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

class Solution {
    fun flipgame(fronts: IntArray, backs: IntArray): Int {
        var same = HashSet<Int>()
        for (i in 0 until fronts.size) {
            if (fronts[i] == backs[i]) same.add(fronts[i])
        }
        var best = Int.MAX_VALUE
        for (x in fronts) { if (!same.contains(x)) best = minOf(best, x) }
        for (x in backs) { if (!same.contains(x)) best = minOf(best, x) }
        return best ==if (Int.MAX_VALUE) 0 else best
    }
}
