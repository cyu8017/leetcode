// LeetCode 1981
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

class Solution {
    fun minimizeTheDifference(mat: Array<IntArray>, target: Int): Int {
        var possible = setOf(0)
        for (row in mat) {
            val nxt = HashSet<Int>()
            val uniq = row.toHashSet()
            for (s in possible) for (x in uniq) nxt.add(s + x)
            val kept = nxt.filter { it <= target }.toHashSet()
            val above = nxt.filter { it > target }
            if (above.isNotEmpty()) kept.add(above.minOrNull()!!)
            possible = if (kept.isNotEmpty()) kept else setOf(nxt.minOrNull()!!)
        }
        return possible.minOf { kotlin.math.abs(it - target) }
    }
}
