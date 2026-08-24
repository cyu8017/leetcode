// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

class Solution {
    fun beforeAndAfterPuzzles(phrases: Array<String>): List<String> {
        val split = Array(phrases.size) { phrases[it].split(" ") }
        val result = sortedSetOf<String>()
        for (i in split.indices) {
            for (j in split.indices) {
                if (i == j) continue
                if (split[i].last() == split[j][0]) {
                    val sb = StringBuilder()
                    for (k in split[i].indices) {
                        if (k > 0) sb.append(' ')
                        sb.append(split[i][k])
                    }
                    for (k in 1 until split[j].size) {
                        sb.append(' ').append(split[j][k])
                    }
                    result.add(sb.toString())
                }
            }
        }
        return result.toList()
    }
}
