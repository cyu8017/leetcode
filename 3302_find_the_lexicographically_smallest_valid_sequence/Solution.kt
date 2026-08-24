// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

class Solution {
    private fun canFinish(w1: String, w2: String, i: Int, j: Int, usedSkip: Boolean, right: IntArray): Boolean {
        val m = w2.length
        if (j >= m) return true
        if (!usedSkip) {
            if (right[j] >= i) return true
            if (j + 1 <= m && right[j + 1] > i) return true
            if (right[j] > i) return true
            return false
        }
        return right[j] >= i
    }

    fun validSequence(word1: String, word2: String): IntArray {
        val n = word1.length
        val m = word2.length
        val right = IntArray(m + 1)
        right[m] = n
        var j = m - 1
        var i = n - 1
        while (i >= 0 && j >= 0) {
            if (word1[i] == word2[j]) {
                right[j] = i
                j--
            }
            i--
        }
        while (j >= 0) {
            right[j] = -1
            j--
        }
        val ans = IntArray(m)
        var usedSkip = false
        i = 0
        j = 0
        while (j < m) {
            var found = false
            while (i < n) {
                if (word1[i] == word2[j]) {
                    if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right)) {
                        ans[j] = i
                        i++
                        found = true
                        break
                    }
                } else if (!usedSkip) {
                    if (canFinish(word1, word2, i + 1, j + 1, true, right)) {
                        ans[j] = i
                        i++
                        usedSkip = true
                        found = true
                        break
                    }
                }
                i++
            }
            if (!found) return IntArray(0)
            j++
        }
        return ans
    }
}
