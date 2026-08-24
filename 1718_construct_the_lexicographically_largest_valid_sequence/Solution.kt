// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution {
    fun constructDistancedSequence(n: Int): IntArray {
        val ans = IntArray(2 * n - 1)
        val used = BooleanArray(n + 1)

        fun backtrack(start: Int): Boolean {
            var i = start
            while (i < ans.size && ans[i] != 0) {
                i++
            }
            if (i == ans.size) {
                return true
            }
            for (value in n downTo 1) {
                if (used[value]) {
                    continue
                }
                if (value == 1) {
                    ans[i] = 1
                    used[1] = true
                    if (backtrack(i + 1)) {
                        return true
                    }
                    used[1] = false
                    ans[i] = 0
                } else {
                    val j = i + value
                    if (j < ans.size && ans[j] == 0) {
                        ans[i] = value
                        ans[j] = value
                        used[value] = true
                        if (backtrack(i + 1)) {
                            return true
                        }
                        used[value] = false
                        ans[i] = 0
                        ans[j] = 0
                    }
                }
            }
            return false
        }

        backtrack(0)
        return ans
    }
}
