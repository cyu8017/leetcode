// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

class Solution {
    private lateinit var words: Array<String>
    private lateinit var letters: IntArray
    private var m = 0
    private var best = 1_000_000_000
    private val freq = IntArray(26)
    private var bestFreqs: MutableList<IntArray> = ArrayList()

    fun supersequences(words: Array<String>): List<List<Int>> {
        this.words = words
        val used = BooleanArray(26)
        for (w in words) {
            used[w[0] - 'a'] = true
            used[w[1] - 'a'] = true
        }
        val lettersList = ArrayList<Int>()
        for (i in 0 until 26) if (used[i]) lettersList.add(i)
        m = lettersList.size
        letters = IntArray(m) { lettersList[it] }
        best = 1_000_000_000
        bestFreqs = ArrayList()
        freq.fill(0)
        dfs(0)
        val res = ArrayList<List<Int>>()
        for (f in bestFreqs) {
            val row = ArrayList<Int>()
            for (v in f) row.add(v)
            res.add(row)
        }
        return res
    }

    private fun dfs(i: Int) {
        if (i == m) {
            for (w in words) {
                val a = w[0] - 'a'
                val b = w[1] - 'a'
                if (a == b) {
                    if (freq[a] < 2) return
                } else if (freq[a] < 1 || freq[b] < 1) return
            }
            var sum = 0
            val f = IntArray(26)
            for (j in 0 until 26) {
                f[j] = freq[j]
                sum += freq[j]
            }
            if (sum < best) {
                best = sum
                bestFreqs = ArrayList()
                bestFreqs.add(f)
            } else if (sum == best) bestFreqs.add(f)
            return
        }
        val L = letters[i]
        for (c in 1..2) {
            freq[L] = c
            dfs(i + 1)
        }
        freq[L] = 0
    }
}
