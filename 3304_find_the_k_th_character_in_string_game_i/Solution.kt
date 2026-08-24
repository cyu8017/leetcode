// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution {
    fun kthCharacter(k: Int): Char {
        var s = StringBuilder("a")
        while (s.length < k) {
            var n = s.length
            for (i in 0 until n) { s.append((char) ('a' + ((s[i] - 'a' + 1) % 26))) }
        }
        return s[k - 1]
    }
}
