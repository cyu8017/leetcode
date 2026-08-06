// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker(arr: Array[Int]) {
  private val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
  for (i <- arr.indices) {
    pos.getOrElseUpdate(arr(i), scala.collection.mutable.ArrayBuffer.empty) += i
  }

  def query(left: Int, right: Int, threshold: Int): Int = {
    var candidate = 0
    var count = 0
    for (i <- left to right) {
      if (count == 0) candidate = arr(i)
      count += (if (arr(i) == candidate) 1 else -1)
    }
    val locs = pos(candidate)
    def lower(x: Int): Int = {
      var lo = 0
      var hi = locs.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (locs(mid) < x) lo = mid + 1 else hi = mid
      }
      lo
    }
    def upper(x: Int): Int = {
      var lo = 0
      var hi = locs.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (locs(mid) <= x) lo = mid + 1 else hi = mid
      }
      lo
    }
    val freq = upper(right) - lower(left)
    if (freq >= threshold) candidate else -1
  }
}
