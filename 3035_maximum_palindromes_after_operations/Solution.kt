// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

class Solution {
    private fun popcount(x0: Int): Int {
        var x = x0
        var c = 0
        while (x != 0) {
            c += x and 1
            x = x shr 1
        }
        return c
    }

    fun maxPalindromesAfterOperations(words: Array<String>): Int {
        var s = 0
        var mask = 0
        for (w in words) {
            s += w.length
            for (ch in w) mask = mask xor (1 shl (ch - 'a'))
        }
        s -= popcount(mask)
        words.sortBy { it.length }
        var ans = 0
        for (w in words) {
            s -= w.length / 2 * 2
            if (s < 0) break
            ans++
        }
        return ans
    }
}
