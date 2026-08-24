// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

class Solution {
    fun simulationResult(windows: IntArray, queries: IntArray): IntArray {
        var n = windows.size
        var s = BooleanArray(n + 1)
        var ans = ArrayList<Int>()
        for (i in queries.size - 1 downTo 0) {
            var q = queries[i]
            if (!s[q]) {
                s[q] = true
                ans.add(q)
            }
        }
        for (w in windows) {
            if (!s[w]) ans.add(w)
        }
        var res = IntArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }
}
