// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

class Solution {
    fun fullJustify(words: Array<String>, maxWidth: Int): List<String> {
        val result = mutableListOf<String>()
        var i = 0

        while (i < words.size) {
            val lineWords = mutableListOf<String>()
            var lineLen = 0

            while (i < words.size) {
                val word = words[i]
                val extra = if (lineWords.isEmpty()) 0 else 1
                if (lineLen + word.length + extra > maxWidth) {
                    break
                }
                lineWords.add(word)
                lineLen += word.length + extra
                i++
            }

            if (i == words.size || lineWords.size == 1) {
                var line = lineWords.joinToString(" ")
                line += " ".repeat(maxWidth - line.length)
                result.add(line)
            } else {
                val totalChars = lineWords.sumOf { it.length }
                val totalSpaces = maxWidth - totalChars
                val gaps = lineWords.size - 1
                val space = totalSpaces / gaps
                val remainder = totalSpaces % gaps
                val line = buildString {
                    for (j in 0 until lineWords.size - 1) {
                        append(lineWords[j])
                        append(" ".repeat(space + if (j < remainder) 1 else 0))
                    }
                    append(lineWords.last())
                }
                result.add(line)
            }
        }

        return result
    }
}
