// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter(words: Array<String>) {
    private val lookup = HashMap<String, Int>()

    init {
        for (index in words.indices) {
            val word = words[index]
            val size = word.length
            for (i in 0..size) {
                for (j in 0..size) {
                    lookup[word.substring(0, i) + "#" + word.substring(j)] = index
                }
            }
        }
    }

    fun f(pref: String, suff: String): Int = lookup.getOrDefault(pref + "#" + suff, -1)
}
