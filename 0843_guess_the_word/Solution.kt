// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

interface Master {
    fun guess(word: String): Int
}

class Solution {
    fun findSecretWord(words: Array<String>, master: Master) {
        var candidates = words.toMutableList()
        while (candidates.isNotEmpty()) {
            var best = candidates[0]
            var bestWorst = candidates.size + 1
            for (w in candidates) {
                val buckets = IntArray(7)
                for (c in candidates) buckets[match(w, c)]++
                var worst = 0
                for (b in buckets) worst = maxOf(worst, b)
                if (worst < bestWorst) {
                    bestWorst = worst
                    best = w
                }
            }
            val score = master.guess(best)
            if (score == 6) return
            val next = ArrayList<String>()
            for (c in candidates) if (match(c, best) == score) next.add(c)
            candidates = next
        }
    }

    private fun match(a: String, b: String): Int {
        var m = 0
        for (i in a.indices) if (a[i] == b[i]) m++
        return m
    }
}
