// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution {
    fun numDifferentIntegers(word: String): Int {
        val seen = HashSet<String>()
        var i = 0
        while (i < word.length) {
            if (!word[i].isDigit()) {
                i++
                continue
            }
            val start = i
            while (i < word.length && word[i].isDigit()) i++
            var j = start
            while (j < i - 1 && word[j] == '0') j++
            seen.add(word.substring(j, i))
        }
        return seen.size
    }
}
