// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

object Solution {
  def findBestValue(arr: Array[Int], target: Int): Int = {
    var lo = 0
    var hi = if (arr.isEmpty) 0 else arr.max
    while (lo < hi) {
      val mid = (lo + hi) / 2
      var sum = 0L
      for (x <- arr) sum += math.min(x, mid).toLong
      if (sum < target) lo = mid + 1 else hi = mid
    }
    var before = 0L
    var after = 0L
    for (x <- arr) {
      before += math.min(x, lo - 1).toLong
      after += math.min(x, lo).toLong
    }
    if (target - before <= after - target) lo - 1 else lo
  }
}
