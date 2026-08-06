// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

object Solution {
  def outerTrees(trees: Array[Array[Int]]): Array[Double] = {
    val pts = scala.util.Random.shuffle(trees.map(p => (p(0).toDouble, p(1).toDouble)).toBuffer)

    def dist(a: (Double, Double), b: (Double, Double)): Double =
      math.hypot(a._1 - b._1, a._2 - b._2)

    def circle2(a: (Double, Double), b: (Double, Double)): ((Double, Double), Double) = {
      val c = ((a._1 + b._1) / 2, (a._2 + b._2) / 2)
      (c, dist(a, b) / 2)
    }

    def circle3(a: (Double, Double), b: (Double, Double), c: (Double, Double)): ((Double, Double), Double) = {
      val (ax, ay) = a
      val (bx, by) = b
      val (cx, cy) = c
      val d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
      if (math.abs(d) < 1e-12) {
        val candidates = Seq(circle2(a, b), circle2(a, c), circle2(b, c))
        return candidates.minBy(_._2)
      }
      val ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
      val uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
      val center = (ux, uy)
      (center, dist(center, a))
    }

    def inside(cir: ((Double, Double), Double), p: (Double, Double)): Boolean =
      dist(cir._1, p) <= cir._2 + 1e-9

    var circle: ((Double, Double), Double) = null
    for (i <- pts.indices) {
      val p = pts(i)
      if (circle == null || !inside(circle, p)) {
        circle = (p, 0.0)
        for (j <- 0 until i) {
          val q = pts(j)
          if (!inside(circle, q)) {
            circle = circle2(p, q)
            for (k <- 0 until j) {
              val r = pts(k)
              if (!inside(circle, r)) circle = circle3(p, q, r)
            }
          }
        }
      }
    }
    Array(circle._1._1, circle._1._2, circle._2)
  }
}
