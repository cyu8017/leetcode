// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

class Solution {
    fun countWordOccurrences(chunks: Array<String>, queries: Array<String>): IntArray {
        val sb = StringBuilder()
        for (c in chunks) sb.append(c)
        val s = sb.toString()
        val n = s.length
        val cnt = HashMap<String, Int>()
        var i = 0
        while (i < n) {
            if (s[i] == ' ' || s[i] == '-') {
                i++
                continue
            }
            var j = i
            while (j < n && s[j] != ' ' && (s[j] != '-' || (j + 1 < n && s[j + 1] != ' ' && s[j + 1] != '-'))) {
                j++
            }
            val word = s.substring(i, j)
            cnt[word] = cnt.getOrDefault(word, 0) + 1
            i = j
        }
        val ans = IntArray(queries.size)
        for (k in queries.indices) ans[k] = cnt.getOrDefault(queries[k], 0)
        return ans
    }
}
