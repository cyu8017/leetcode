// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

object Solution {
  def makeArrayIncreasing(arr1: Array[Int], arr2: Array[Int]): Int = {
    val sorted2 = arr2.distinct.sorted
    var dp = Map(-1 -> 0)
    for (num <- arr1) {
      val newDp = scala.collection.mutable.Map.empty[Int, Int]
      for ((prev, ops) <- dp) {
        if (num > prev) newDp(num) = math.min(newDp.getOrElse(num, Int.MaxValue), ops)
        var lo = 0
        var hi = sorted2.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (sorted2(mid) <= prev) lo = mid + 1 else hi = mid
        }
        if (lo < sorted2.length) {
          val chosen = sorted2(lo)
          newDp(chosen) = math.min(newDp.getOrElse(chosen, Int.MaxValue), ops + 1)
        }
      }
      dp = newDp.toMap
      if (dp.isEmpty) return -1
    }
    dp.values.min
  }
}
