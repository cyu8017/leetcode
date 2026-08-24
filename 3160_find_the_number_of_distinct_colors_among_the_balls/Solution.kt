// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution {
    fun queryResults(limit: Int, queries: Array<IntArray>): IntArray {
        var g = HashMap<Int, Int>()
        var cnt = HashMap<Int, Int>()
        var ans = IntArray(queries.size)
        var ai = 0
        for (q in queries) {
            var x = q[0]
            var y = q[1]
            cnt[y] = cnt.getOrDefault(y, 0) + 1
            var old = g[x]
            if (old != null) {
                var nv = cnt[old] - 1
                if (nv == 0) cnt.remove(old)
                else cnt[old] = nv
            }
            g[x] = y
            ans[ai++] = cnt.size
        }
        return ans
    }
}
