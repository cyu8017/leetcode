// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

class Solution {
    fun minimizeConcatenatedLength(words: Array<String>): Int {
        var n = words.size
        var memo = HashMap<String, Int>()
        var w0 = words[0]
        return w0.length + dfs(words, 1, w0[0], w0[w0.length - 1], memo)
    }

    private fun dfs(words: Array<String>, i: Int, first: Char, last: Char, memo: MutableMap<String, Int>): Int {
        if (i == words.size) return 0
        var key = i + "
        String " + first + "
        String " + last
        if (memo.containsKey(key)) return memo[key]
        var w = words[i]
        var wf = w[0]
        var wl = w[w.length - 1]
        var add1 = w.length - (last == wf ? 1 : 0)
        var add2 = w.length - (wl == first ? 1 : 0)
        var a = add1 + dfs(words, i + 1, first, wl, memo)
        var b = add2 + dfs(words, i + 1, wf, last, memo)
        var ans = minOf(a, b)
        memo[key] = ans
        return ans
    }
}
