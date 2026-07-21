// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

class Solution {
    fun earliestAndLatest(n: Int, firstPlayer: Int, secondPlayer: Int): IntArray {
        val first = firstPlayer
        val second = secondPlayer
        val memo = HashMap<List<Int>, IntArray>()

        fun dfs(players: List<Int>): IntArray {
            memo[players]?.let { return it }
            val count = players.size
            val firstIndex = players.indexOf(first)
            val secondIndex = players.indexOf(second)
            if (firstIndex + secondIndex == count - 1) {
                return intArrayOf(1, 1).also { memo[players] = it }
            }
            val choices = mutableListOf<List<Int>>()
            for (index in 0 until count / 2) {
                val left = players[index]
                val right = players[count - 1 - index]
                when {
                    left == first || left == second -> choices.add(listOf(left))
                    right == first || right == second -> choices.add(listOf(right))
                    else -> choices.add(listOf(left, right))
                }
            }
            if (count % 2 == 1) {
                choices.add(listOf(players[count / 2]))
            }
            var earliest = Int.MAX_VALUE / 2
            var latest = 0
            fun explore(i: Int, picks: MutableList<Int>) {
                if (i == choices.size) {
                    val winners = picks.sorted()
                    val (early, late) = dfs(winners)
                    earliest = minOf(earliest, early + 1)
                    latest = maxOf(latest, late + 1)
                    return
                }
                for (pick in choices[i]) {
                    picks.add(pick)
                    explore(i + 1, picks)
                    picks.removeAt(picks.lastIndex)
                }
            }
            explore(0, mutableListOf())
            return intArrayOf(earliest, latest).also { memo[players] = it }
        }

        return dfs((1..n).toList())
    }
}
