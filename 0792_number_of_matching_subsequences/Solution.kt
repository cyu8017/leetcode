// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

class Solution {
    fun numMatchingSubseq(s: String, words: Array<String>): Int {
        val waiting = Array(26) { ArrayList<IntArray>() }
        for (i in words.indices) {
            val w = words[i]
            waiting[w[0] - 'a'].add(intArrayOf(i, 0))
        }
        var ans = 0
        for (ch in s) {
            val cur = waiting[ch - 'a']
            waiting[ch - 'a'] = ArrayList()
            for (it in cur) {
                val wi = it[0]
                val idx = it[1] + 1
                if (idx == words[wi].length) ans++
                else waiting[words[wi][idx] - 'a'].add(intArrayOf(wi, idx))
            }
        }
        return ans
    }
}
