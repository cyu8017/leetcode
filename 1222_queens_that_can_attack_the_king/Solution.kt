// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution {
    fun queensAttacktheKing(queens: Array<IntArray>, king: IntArray): List<List<Int>> {
        val occupied = queens.map { it[0] to it[1] }.toSet()
        val answer = mutableListOf<List<Int>>()
        for (dr in -1..1) {
            for (dc in -1..1) {
                if (dr == 0 && dc == 0) continue
                var r = king[0] + dr
                var c = king[1] + dc
                while (r in 0..7 && c in 0..7) {
                    if (r to c in occupied) {
                        answer.add(listOf(r, c))
                        break
                    }
                    r += dr
                    c += dc
                }
            }
        }
        return answer
    }
}
