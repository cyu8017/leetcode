// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

object Solution {
  def maxFrequency(nums: Array[Int], k: Int): Int = {
    var base = 0
    nums.foreach { x => if (x == k) base += 1 }
    var ans = base
    val uniq = scala.collection.mutable.Set.empty[Int]
    nums.foreach(x => uniq += x)
    uniq.foreach { v =>
      if (v != k) {
        var best = 0
        var cur = 0
        nums.foreach { x =>
          var delta = 0
          if (x == v) delta = 1
          else if (x == k) delta = -1
          cur += delta
          if (cur < 0) cur = 0
          if (cur > best) best = cur
        }
        if (base + best > ans) ans = base + best
      }
    }
    ans
  }
}
