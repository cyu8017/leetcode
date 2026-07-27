// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

class Solution {
    fun decrypt(code: IntArray, k: Int): IntArray {
        val n = code.size
        if (k == 0) return IntArray(n)
        val a = IntArray(n * 2) { code[it % n] }
        val ans = IntArray(n)
        for (i in 0 until n) {
            ans[i] = if (k > 0) {
                (i + 1 until i + k + 1).sumOf { a[it] }
            } else {
                (i + n + k until i + n).sumOf { a[it] }
            }
        }
        return ans
    }
}
