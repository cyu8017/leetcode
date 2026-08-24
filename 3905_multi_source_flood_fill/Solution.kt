// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

class Solution {
    fun colorGrid(n: Int, m: Int, sources: Array<IntArray>): Array<IntArray> {
        var ans = Array(n) { IntArray(m) }
        var q = ArrayList<IntArray>()
        for (s in sources) { q.add(s) }
        var dirs = { -1, 0, 1, 0, -1 }
        for (s in q) { ans[s[0]][s[1]] = s[2] }
        while (!q.isEmpty()) {
            var vis = TreeMap<Long, Int>()
            for (curr in q) {
                var r = curr[0]
                var c = curr[1]
                var color = curr[2]
                for (i in 0 until 4) {
                    var x = r + dirs[i]
                    var y = c + dirs[i + 1]
                    if (x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0) {
                        var key = (x  shl  32) | (y & 0xffffffffL)
                        if (!vis.containsKey(key) || color > vis[key]) vis[key] = color
                    }
                }
            }
            q.clear()
            for (kv in vis) {
                var key = kv.key
                var x = (key  shr  32)
                var y = key
                var color = kv.value
                ans[x][y] = color
                q.add(intArrayOf( x, y, color ))
            }
        }
        return ans
    }
}
