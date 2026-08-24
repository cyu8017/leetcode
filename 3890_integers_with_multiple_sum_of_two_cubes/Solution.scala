// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

object Solution {
  private var GOOD: Array[Int] = _
  private var ready = false

  private def init(): Unit = {
    if (ready) return
    val LIMIT = 1000000000L
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val cubes = new Array[Long](1001)
    var i = 0
    while (i <= 1000) {
      cubes(i) = i.toLong * i * i
      i += 1
    }
    var a = 1
    while (a <= 1000) {
      var b = a
      var stop = false
      while (b <= 1000 && !stop) {
        val x = cubes(a) + cubes(b)
        if (x > LIMIT) stop = true
        else {
          val xi = x.toInt
          cnt(xi) = cnt.getOrElse(xi, 0) + 1
        }
        b += 1
      }
      a += 1
    }
    val buf = scala.collection.mutable.ArrayBuffer.empty[Int]
    cnt.foreach { case (k, v) => if (v > 1) buf += k }
    GOOD = buf.sorted.toArray
    ready = true
  }

  def findGoodIntegers(n: Int): Array[Int] = {
    init()
    var lo = 0
    var hi = GOOD.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (GOOD(mid) <= n) lo = mid + 1
      else hi = mid
    }
    java.util.Arrays.copyOf(GOOD, lo)
  }
}
