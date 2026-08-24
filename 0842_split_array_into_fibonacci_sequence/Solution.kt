// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution {
    private var num: String? = null
    private var path: MutableList<Int>? = null

    fun splitIntoFibonacci(num: String): MutableList<Int> {
        var num = num
        this.num = num
        path = ArrayList()
        dfs(0)
        return path
    }

    private fun dfs(start: Int): Boolean {
        var n = num.length
        if (start == n) return path.size() >= 3
        var `val` = 0
        for (end in start until n) {
            if (num[start] == '0' && end > start) break
            val = val * 10 + (num[end] - '0')
            if (val > Int.MAX_VALUE) break
            if (path.size >= 2) {
                var total = path[path.size - 1] + path[path.size - 2]
                if (val < total) continue
                if (val > total) break
            }
            path.add(val)
            if (dfs(end + 1)) return true
            path.remove(path.size - 1)
        }
        return false
    }
}
