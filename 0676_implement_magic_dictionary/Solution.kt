// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/


class MagicDictionary {
    private val words = ArrayList<String>()

    fun buildDict(dictionary: Array<String>) {
        words.clear()
        words.addAll(dictionary)
    }

    fun search(searchWord: String): Boolean {
        for (word in words) {
            if (word.length != searchWord.length) continue
            var diff = 0
            for (i in word.indices) {
                if (word[i] != searchWord[i] && ++diff > 1) break
            }
            if (diff == 1) return true
        }
        return false
    }
}
