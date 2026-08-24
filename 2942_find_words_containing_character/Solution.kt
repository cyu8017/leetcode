// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

class Solution {
    fun findWordsContaining(words: Array<String>, x: Char): MutableList<Int> {
        var ans = ArrayList<Int>()
        for (i in 0 until words.size) {
            if (words[i].indexOf(x) >= 0) ans.add(i)
        }
        return ans
    }
}
