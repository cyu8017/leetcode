// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

class Solution {
    fun expressiveWords(s: String, words: Array<String>): Int {
        var target = groups(s)
        var ans = 0
        for (word in words) {
            var source = groups(word)
            if (source.size != target.size) continue
            var ok = true
            for (i in 0 until source.size) {
                if (source.get(i)[0] != target.get(i)[0]) { ok = false; break; }
                var c1 = source[i][1], c2 = target[i][1]
                if (c1 > c2 || (c1 != c2 && c2 < 3)) { ok = false; break; }
            }
            if (ok) ans++
        }
        return ans
    }

    private fun groups(text: String): MutableList<IntArray> {
        var result = ArrayList<IntArray>()
        var i = 0, n = text.length
        while (i < n) {
            var j = i
            while (j < n && text[j] == text[i]) j++
            result.add(intArrayOf(text[i], j - i))
            i = j
        }
        return result
    }
}
