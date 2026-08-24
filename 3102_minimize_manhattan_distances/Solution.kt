// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

class Solution {
    private fun merge(st: TreeMap<Int, Int>, x: Int, v: Int) {
        var nv = st.getOrDefault(x, 0) + v
        if (nv == 0) st.remove(x)
        else st[x] = nv
    }

    fun minimumDistance(points: Array<IntArray>): Int {
        var st1 = TreeMap<Int, Int>()
        var st2 = TreeMap<Int, Int>()
        for (p in points) {
            merge(st1, p[0] + p[1], 1)
            merge(st2, p[0] - p[1], 1)
        }
        var ans = Int.MAX_VALUE
        for (p in points) {
            var x = p[0]
            var y = p[1]
            merge(st1, x + y, -1)
            merge(st2, x - y, -1)
            ans = minOf(ans, maxOf(st1.lastKey() - st1.firstKey(), st2.lastKey() - st2.firstKey()))
            merge(st1, x + y, 1)
            merge(st2, x - y, 1)
        }
        return ans
    }
}
