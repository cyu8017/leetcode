// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

class Solution {
    fun generateSentences(synonyms: List<List<String>>, text: String): List<String> {
        val parent = mutableMapOf<String, String>()
        fun find(x: String): String {
            parent.putIfAbsent(x, x)
            if (parent[x] != x) parent[x] = find(parent[x]!!)
            return parent[x]!!
        }
        for (pair in synonyms) {
            val a = find(pair[0])
            val b = find(pair[1])
            parent[a] = b
        }
        val groups = mutableMapOf<String, MutableList<String>>()
        for (word in parent.keys) {
            groups.getOrPut(find(word)) { mutableListOf() }.add(word)
        }
        for (g in groups.values) g.sort()
        val tokens = text.split(" ")
        val choices = tokens.map { w ->
            if (w in parent) groups[find(w)]!! else listOf(w)
        }
        val answer = mutableListOf<String>()
        fun backtrack(idx: Int, cur: MutableList<String>) {
            if (idx == choices.size) {
                answer.add(cur.joinToString(" "))
                return
            }
            for (w in choices[idx]) {
                cur.add(w)
                backtrack(idx + 1, cur)
                cur.removeAt(cur.lastIndex)
            }
        }
        backtrack(0, mutableListOf())
        return answer
    }
}
