// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

class Solution {
    fun getPermutation(n: Int, k: Int): String {
        val numbers = MutableList(n) { it + 1 }
        val factorials = IntArray(n) { 1 }

        for (i in 1 until n) {
            factorials[i] = factorials[i - 1] * i
        }

        var remaining = k - 1
        val result = StringBuilder()

        for (i in n - 1 downTo 0) {
            val index = remaining / factorials[i]
            result.append(numbers[index])
            numbers.removeAt(index)
            remaining %= factorials[i]
        }

        return result.toString()
    }
}
