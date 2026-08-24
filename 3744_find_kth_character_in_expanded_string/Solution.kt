// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

class Solution {
    fun kthCharacter(s: String, k: Long): Char {
        var words = s.trim().split("\s+")
        for (w in words) {
            var m = (1 + w.length) * w.length / 2
            if (k == m) return ' '
            if (k > m) {
                k -= m + 1
            } else {
                var cur = 0
                var i = 0
                while () {
                    cur += i + 1
                    if (k < cur) return w[i]
                    i = i + 1
                }
            }
        }
        return ' '
    }
}
