// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class Solution {
    fun findNumOfValidWords(words: Array<String>, puzzles: Array<String>): List<Int> {
        val freq = mutableMapOf<Int, Int>()
        for (w in words) {
            val m = maskOf(w)
            freq[m] = freq.getOrDefault(m, 0) + 1
        }
        val ans = mutableListOf<Int>()
        for (puzzle in puzzles) {
            val first = 1 shl (puzzle[0] - 'a')
            val full = maskOf(puzzle)
            var sub = full
            var total = 0
            while (true) {
                if (sub and first != 0) total += freq.getOrDefault(sub, 0)
                if (sub == 0) break
                sub = (sub - 1) and full
            }
            ans.add(total)
        }
        return ans
    }

    private fun maskOf(s: String): Int {
        var mask = 0
        for (ch in s) mask = mask or (1 shl (ch - 'a'))
        return mask
    }
}
