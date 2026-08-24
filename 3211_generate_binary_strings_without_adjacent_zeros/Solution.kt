// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution {
    private var n = 0
    private lateinit var t: StringBuilder
    private lateinit var ans: MutableList<String>

    fun validStrings(n: Int): List<String> {
        this.n = n
        ans = ArrayList()
        t = StringBuilder()
        dfs(0)
        return ans
    }

    private fun dfs(i: Int) {
        if (i >= n) {
            ans.add(t.toString())
            return
        }
        for (j in 0 until 2) {
            if ((j == 0 && (i == 0 || t[i - 1] == '1')) || j == 1) {
                t.append(('0'.code + j).toChar())
                dfs(i + 1)
                t.deleteCharAt(t.length - 1)
            }
        }
    }
}
