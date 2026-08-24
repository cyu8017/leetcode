// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

class Solution {
    fun toGoatLatin(sentence: String): String {
        val vowels = hashSetOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        val words = sentence.split(" ")
        val out = StringBuilder()
        for (i in words.indices) {
            if (i > 0) out.append(' ')
            val word = words[i]
            val goat = StringBuilder()
            if (vowels.contains(word[0])) goat.append(word).append("ma")
            else goat.append(word.substring(1)).append(word[0]).append("ma")
            repeat(i + 1) { goat.append('a') }
            out.append(goat)
        }
        return out.toString()
    }
}
