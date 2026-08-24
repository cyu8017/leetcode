// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery(_arr: Array[Int]) {
  private val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
  var i = 0
  while (i < _arr.length) {
    pos.getOrElseUpdate(_arr(i), scala.collection.mutable.ArrayBuffer.empty[Int]) += i
    i += 1
  }

  def query(left: Int, right: Int, value: Int): Int = {
    val p = pos.getOrElse(value, return 0)
    upper(p, right) - lower(p, left)
  }

  private def lower(p: scala.collection.mutable.ArrayBuffer[Int], x: Int): Int = {
    var lo = 0
    var hi = p.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (p(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }

  private def upper(p: scala.collection.mutable.ArrayBuffer[Int], x: Int): Int = {
    var lo = 0
    var hi = p.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (p(mid) <= x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
