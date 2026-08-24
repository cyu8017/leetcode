// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

class Solution {
    fun minimumLengthEncoding(words: Array<String>): Int {
        var good = HashSet(words))
        for (word in words) {
            for (i in 1 until word.length) { good.remove(word.substring(i)) }
        }
        var ans = 0
        for (word in good) { ans += word.length + 1 }
        return ans
    }
}
