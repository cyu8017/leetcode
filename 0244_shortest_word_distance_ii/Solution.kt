// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

class WordDistance(private val positions: Map<String, List<Int>>) {
    constructor(wordsDict: Array<String>) : this(
        buildMap {
            wordsDict.forEachIndexed { index, word ->
                getOrPut(word) { mutableListOf() }.add(index)
            }
        }
    )

    fun shortest(word1: String, word2: String): Int {
        val left = positions.getValue(word1)
        val right = positions.getValue(word2)
        var i = 0
        var j = 0
        var best = Int.MAX_VALUE
        while (i < left.size && j < right.size) {
            best = minOf(best, kotlin.math.abs(left[i] - right[j]))
            if (left[i] <= right[j]) {
                i++
            } else {
                j++
            }
        }
        return best
    }
}
