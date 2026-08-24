// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
    fun mostWordsFound(sentences: Array<String>): Int {
        var ans: Int = 0
        for (s in sentences) {
            var c: Int = 1
            for (i in 0 until s.length) if (s[i] == ' ') c++
            ans = maxOf(ans, c)
        }
        return ans
    }
}
