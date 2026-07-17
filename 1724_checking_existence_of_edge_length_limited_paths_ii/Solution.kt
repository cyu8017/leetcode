// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

class DistanceLimitedPathsExist(n: Int, edgeList: Array<IntArray>) {
    private val weights = ArrayList<Int>()
    private val versions = ArrayList<IntArray>()

    init {
        val edges = edgeList
            .map { intArrayOf(it[2], it[0], it[1]) }
            .sortedWith(compareBy({ it[0] }, { it[1] }, { it[2] }))
        val parent = IntArray(n) { it }
        val size = IntArray(n) { 1 }
        fun find(start: Int): Int {
            var x = start
            while (parent[x] != x) {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        var i = 0
        while (i < edges.size) {
            val weight = edges[i][0]
            while (i < edges.size && edges[i][0] == weight) {
                var ra = find(edges[i][1])
                var rb = find(edges[i][2])
                if (ra != rb) {
                    if (size[ra] < size[rb]) {
                        val tmp = ra
                        ra = rb
                        rb = tmp
                    }
                    parent[rb] = ra
                    size[ra] += size[rb]
                }
                i++
            }
            weights.add(weight)
            versions.add(parent.clone())
        }
    }

    fun query(p: Int, q: Int, limit: Int): Boolean {
        var lo = 0
        var hi = weights.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (weights[mid] < limit) lo = mid + 1 else hi = mid
        }
        val idx = lo - 1
        if (idx < 0) return p == q
        val parent = versions[idx]
        var rp = p
        while (parent[rp] != rp) rp = parent[rp]
        var rq = q
        while (parent[rq] != rq) rq = parent[rq]
        return rp == rq
    }
}
