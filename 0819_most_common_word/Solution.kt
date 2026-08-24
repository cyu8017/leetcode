// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

class Solution {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        var bannedSet = HashSet(banned))
        var counts = HashMap<String, Int>()
        var word = StringBuilder()
        var best = ""
        var bestCount = 0
        for (i in 0 until = paragraph.length) {
            var ch = if (i < paragraph.length) paragraph[i] else ' '
            if (Character.isLetter(ch)) {
                word.append(Character.toLowerCase(ch))
            } else if (word.length() > 0) {
                var w = word.toString()
                word.setLength(0)
                if (!bannedSet.contains(w)) {
                    var c = counts.merge(w, 1, Integer::sum)
                    if (c > bestCount) {
                        bestCount = c
                        best = w
                    }
                }
            }
        }
        return best
    }
}
