// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

class Solution {
    private var xCorner = 0
    private var yCorner = 0
    private lateinit var circles: Array<IntArray>
    private lateinit var vis: BooleanArray
    private var n = 0

    fun canReachCorner(xCorner: Int, yCorner: Int, circles: Array<IntArray>): Boolean {
        this.xCorner = xCorner
        this.yCorner = yCorner
        this.circles = circles
        n = circles.size
        vis = BooleanArray(n)
        for (i in 0 until n) {
            val x = circles[i][0]
            val y = circles[i][1]
            val r = circles[i][2]
            if (inCircle(0, 0, x, y, r) || inCircle(xCorner, yCorner, x, y, r)) return false
            if (!vis[i] && crossLeftTop(x, y, r) && dfs(i)) return false
        }
        return true
    }

    private fun inCircle(x: Int, y: Int, cx: Int, cy: Int, r: Int): Boolean {
        val dx = (x - cx).toLong()
        val dy = (y - cy).toLong()
        return dx * dx + dy * dy <= r.toLong() * r
    }

    private fun crossLeftTop(cx: Int, cy: Int, r: Int): Boolean {
        val a = kotlin.math.abs(cx) <= r && cy in 0..yCorner
        val b = kotlin.math.abs(cy - yCorner) <= r && cx in 0..xCorner
        return a || b
    }

    private fun crossRightBottom(cx: Int, cy: Int, r: Int): Boolean {
        val a = kotlin.math.abs(cx - xCorner) <= r && cy in 0..yCorner
        val b = kotlin.math.abs(cy) <= r && cx in 0..xCorner
        return a || b
    }

    private fun dfs(i: Int): Boolean {
        val x1 = circles[i][0]
        val y1 = circles[i][1]
        val r1 = circles[i][2]
        if (crossRightBottom(x1, y1, r1)) return true
        vis[i] = true
        for (j in 0 until n) {
            if (vis[j]) continue
            val x2 = circles[j][0]
            val y2 = circles[j][1]
            val r2 = circles[j][2]
            if ((x1 - x2).toLong() * (x1 - x2) + (y1 - y2).toLong() * (y1 - y2) >
                (r1 + r2).toLong() * (r1 + r2)
            ) continue
            if (x1.toLong() * r2 + x2.toLong() * r1 < (r1 + r2).toLong() * xCorner &&
                y1.toLong() * r2 + y2.toLong() * r1 < (r1 + r2).toLong() * yCorner &&
                dfs(j)
            ) return true
        }
        return false
    }
}
