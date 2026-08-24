// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution {
    fun findThePrefixCommonArray(A: IntArray, B: IntArray): IntArray {
        val n = A.size
        val seenA = BooleanArray(n + 1)
        val seenB = BooleanArray(n + 1)
        val ans = IntArray(n)
        var common = 0
        for (i in 0 until n) {
            if (seenB[A[i]]) common++
            seenA[A[i]] = true
            if (seenA[B[i]]) common++
            seenB[B[i]] = true
            ans[i] = common
        }
        return ans
    }
}
