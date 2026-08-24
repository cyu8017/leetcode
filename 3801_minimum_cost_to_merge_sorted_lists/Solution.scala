// LeetCode 3801 - Minimum Cost To Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

object Solution {
  def minMergeCost(lists: Array[Array[Int]]): Long = {
    val m = lists.length
    val totalMasks = 1 << m
    val merged = Array.fill(totalMasks)(new java.util.ArrayList[Integer]())
    val length = new Array[Int](totalMasks)
    val median = new Array[Int](totalMasks)
    var mask = 1
    while (mask < totalMasks) {
      val bit = mask & -mask
      val index = Integer.numberOfTrailingZeros(bit)
      val previous = merged(mask ^ bit)
      val current = lists(index)
      val out = new java.util.ArrayList[Integer](previous.size() + current.length)
      var i = 0
      var j = 0
      while (i < previous.size() || j < current.length) {
        if (j == current.length || (i < previous.size() && previous.get(i) <= current(j))) {
          out.add(previous.get(i))
          i += 1
        } else {
          out.add(current(j))
          j += 1
        }
      }
      merged(mask) = out
      length(mask) = out.size()
      median(mask) = out.get((out.size() - 1) / 2)
      mask += 1
    }
    val INF = 1L << 62
    val dp = new Array[Long](totalMasks)
    mask = 1
    while (mask < totalMasks) {
      if ((mask & (mask - 1)) != 0) {
        dp(mask) = INF
        val firstBit = mask & -mask
        var left = (mask - 1) & mask
        while (left > 0) {
          if ((left & firstBit) != 0) {
            val right = mask ^ left
            if (right != 0) {
              var diff = median(left) - median(right)
              if (diff < 0) diff = -diff
              val candidate = dp(left) + dp(right) + length(mask) + diff
              if (candidate < dp(mask)) dp(mask) = candidate
            }
          }
          left = (left - 1) & mask
        }
      }
      mask += 1
    }
    dp(totalMasks - 1)
  }
}
