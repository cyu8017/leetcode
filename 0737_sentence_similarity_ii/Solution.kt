// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

class Solution {
    private val parent = HashMap<String, String>()

    fun areSentencesSimilarTwo(sentence1: Array<String>, sentence2: Array<String>, similarPairs: MutableList<MutableList<String>>): Boolean {
        if (sentence1.size != sentence2.size) return false
        parent.clear()
        for (pair in similarPairs) { unite(pair[0], pair[1]) }
        for (i in 0 until sentence1.size) {
            if (!find(sentence1[(i]) == find(sentence2[i]))) return false
        }
        return true
    }

    private fun find(x: String): String {
        var x = x
        parent.putIfAbsent(x, x)
        while (!parent[(x] == x)) {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    private fun unite(a: String, b: String) {
        parent[find(a)] = find(b)
    }
}
