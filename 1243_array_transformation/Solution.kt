// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

class Solution {
    fun transformArray(arr: IntArray): List<Int> {
        var cur = arr
        while (true) {
            val nxt = cur.copyOf()
            for (i in 1 until cur.size - 1) {
                if (cur[i] < cur[i - 1] && cur[i] < cur[i + 1]) nxt[i]++
                else if (cur[i] > cur[i - 1] && cur[i] > cur[i + 1]) nxt[i]--
            }
            if (nxt.contentEquals(cur)) return cur.toList()
            cur = nxt
        }
    }
}
