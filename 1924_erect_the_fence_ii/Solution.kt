// LeetCode 1924
// https://leetcode.com/problems/erect-the-fence-ii/

import kotlin.math.hypot
import kotlin.math.abs
import kotlin.random.Random

class Solution {
    fun outerTrees(trees: Array<IntArray>): DoubleArray {
        val pts = trees.map { it[0].toDouble() to it[1].toDouble() }.shuffled(Random(0)).toMutableList()

        fun dist(a: Pair<Double, Double>, b: Pair<Double, Double>) =
            hypot(a.first - b.first, a.second - b.second)

        fun circle2(a: Pair<Double, Double>, b: Pair<Double, Double>): Pair<Pair<Double, Double>, Double> {
            val c = (a.first + b.first) / 2 to (a.second + b.second) / 2
            return c to dist(a, b) / 2
        }

        fun circle3(
            a: Pair<Double, Double>,
            b: Pair<Double, Double>,
            c: Pair<Double, Double>
        ): Pair<Pair<Double, Double>, Double> {
            val (ax, ay) = a
            val (bx, by) = b
            val (cx, cy) = c
            val d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if (abs(d) < 1e-12) {
                return listOf(circle2(a, b), circle2(a, c), circle2(b, c)).minBy { it.second }
            }
            val ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
            val uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
            val center = ux to uy
            return center to dist(center, a)
        }

        fun inside(cir: Pair<Pair<Double, Double>, Double>?, p: Pair<Double, Double>): Boolean {
            if (cir == null) return false
            return dist(cir.first, p) <= cir.second + 1e-9
        }

        var circle: Pair<Pair<Double, Double>, Double>? = null
        for (i in pts.indices) {
            val p = pts[i]
            if (circle == null || !inside(circle, p)) {
                circle = p to 0.0
                for (j in 0 until i) {
                    val q = pts[j]
                    if (!inside(circle, q)) {
                        circle = circle2(p, q)
                        for (k in 0 until j) {
                            val r = pts[k]
                            if (!inside(circle, r)) circle = circle3(p, q, r)
                        }
                    }
                }
            }
        }
        val (center, r) = circle!!
        return doubleArrayOf(center.first, center.second, r)
    }
}
