// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution {
    fun robotWithString(s: String): String {
        val n = s.length
        val minSuf = CharArray(n + 1)
        minSuf[n] = ('z'.code + 1).toChar()
        for (i in n - 1 downTo 0) {
            minSuf[i] = if (s[i] < minSuf[i + 1]) s[i] else minSuf[i + 1]
        }
        val stack = ArrayDeque<Char>()
        val ans = StringBuilder()
        for (i in 0 until n) {
            stack.addLast(s[i])
            while (stack.isNotEmpty() && stack.last() <= minSuf[i + 1]) {
                ans.append(stack.removeLast())
            }
        }
        while (stack.isNotEmpty()) ans.append(stack.removeLast())
        return ans.toString()
    }
}
