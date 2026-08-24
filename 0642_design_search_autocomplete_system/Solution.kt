// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

class AutocompleteSystem(sentences: Array<String>, times: IntArray) {
    private val counts = HashMap<String, Int>()
    private val current = StringBuilder()

    init {
        for (i in sentences.indices) {
            counts[sentences[i]] = counts.getOrDefault(sentences[i], 0) + times[i]
        }
    }

    fun input(c: Char): List<String> {
        if (c == '#') {
            val sentence = current.toString()
            counts[sentence] = counts.getOrDefault(sentence, 0) + 1
            current.setLength(0)
            return emptyList()
        }
        current.append(c)
        val prefix = current.toString()
        val matches = ArrayList<String>()
        for (sentence in counts.keys) {
            if (sentence.startsWith(prefix)) matches.add(sentence)
        }
        matches.sortWith(compareByDescending<String> { counts[it]!! }.thenBy { it })
        return if (matches.size > 3) matches.subList(0, 3) else matches
    }
}
