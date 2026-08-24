// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

class Solution {
    fun uniqueMorseRepresentations(words: Array<String>): Int {
        String[] codes = {
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        }
        var seen = HashSet<String>()
        for (word in words) {
            var code = StringBuilder()
            for (ch in word.toCharArray()) { code.append(codes[ch - 'a']) }
            seen.add(code.toString())
        }
        return seen.size
    }
}
