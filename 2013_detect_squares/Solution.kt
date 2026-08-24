// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

class DetectSquares {
    private val cnt = HashMap<Long, Int>()

    private fun key(x: Int, y: Int): Long {
        return (x.toLong() shl 32) xor (y.toLong() and 0xffffffffL)
    }

    fun add(point: IntArray) {
        val k = key(point[0], point[1])
        cnt[k] = cnt.getOrDefault(k, 0) + 1
    }

    fun count(point: IntArray): Int {
        val x = point[0]
        val y = point[1]
        var ans = 0
        for ((k, c) in cnt) {
            val px = (k shr 32).toInt()
            val py = k.toInt()
            if (px == x || py == y) continue
            if (kotlin.math.abs(px - x) != kotlin.math.abs(py - y)) continue
            val c1 = cnt.getOrDefault(key(px, y), 0)
            val c2 = cnt.getOrDefault(key(x, py), 0)
            ans += c * c1 * c2
        }
        return ans
    }
}
