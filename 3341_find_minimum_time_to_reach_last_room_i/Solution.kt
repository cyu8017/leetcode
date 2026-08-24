// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

class Solution {
    fun minTimeToReach(moveTime: Array<IntArray>): Int {
        var m = moveTime.size
        var n = moveTime[0].size
        var dist = Array(m) { IntArray(n) }
        for (row in dist) { row.fill(1  shl  30) }
        var h = PriorityQueue(compareBy { it[0] })
        h.offer(intArrayOf(0, 0, 0))
        dist[0][0] = 0
        var dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
        while (!h.isEmpty()) {
            var cur = h.poll()
            var t = cur[0]
            var r = cur[1]
            var c = cur[2]
            if (t != dist[r][c]) continue
            if (r == m - 1 && c == n - 1) return t
            for (d in dirs) {
                var nr = r + d[0]
                var nc = c + d[1]
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue
                var start = maxOf(t, moveTime[nr][nc])
                var nt = start + 1
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt
                    h.offer(intArrayOf(nt, nr, nc))
                }
            }
        }
        return -1
    }
}
