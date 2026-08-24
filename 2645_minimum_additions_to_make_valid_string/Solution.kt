
// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution {
    fun addMinimum(word: String): Int {
        var ans = 0
        var expect = 0
        var i = 0
        val n = word.length
        while (i < n) {
            val need = ('a'.code + expect).toChar()
            if (word[i] == need) i++ else ans++
            expect = (expect + 1) % 3
        }
        ans += (3 - expect) % 3
        return ans
    }
}
