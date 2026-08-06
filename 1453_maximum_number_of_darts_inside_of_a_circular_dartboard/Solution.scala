object Solution {
  def numPoints(darts: Array[Array[Int]], r: Int): Int = {
    var answer = if (darts.isEmpty) 0 else 1
    for (i <- darts.indices; j <- i + 1 until darts.length) {
      val dx = darts(j)(0) - darts(i)(0); val dy = darts(j)(1) - darts(i)(1)
      val d2 = dx.toDouble * dx + dy.toDouble * dy
      if (d2 <= 4.0 * r * r && d2 > 0) {
        val d = math.sqrt(d2); val h = math.sqrt(r.toDouble * r - d2 / 4)
        val mx = (darts(i)(0) + darts(j)(0)) / 2.0; val my = (darts(i)(1) + darts(j)(1)) / 2.0
        for (sign <- Seq(-1, 1)) {
          val cx = mx + sign * (-dy) * h / d; val cy = my + sign * dx * h / d
          answer = answer.max(darts.count(p => { val x = p(0) - cx; val y = p(1) - cy; x * x + y * y <= r.toDouble * r + 1e-7 }))
        }
      }
    }
    answer
  }
}
