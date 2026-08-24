// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

object Solution {
  def beautifulSubsets(nums: Array[Int], k: Int): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach(x => freq(x) = freq.getOrElse(x, 0) + 1)
    val groups = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    freq.keys.foreach { key =>
      val rem = key % k
      groups.getOrElseUpdate(rem, scala.collection.mutable.ArrayBuffer.empty[Int]) += key
    }
    var ans = 1
    groups.values.foreach { vals =>
      val sorted = vals.sorted
      var prevTake = 0
      var prevSkip = 1
      var prevVal = Int.MinValue / 2
      sorted.foreach { v =>
        var ways = 1
        var i = 0
        while (i < freq(v)) {
          ways *= 2
          i += 1
        }
        ways -= 1
        val skip = prevTake + prevSkip
        var take = ways * prevSkip
        if (prevVal + k != v) take += ways * prevTake
        prevTake = take
        prevSkip = skip
        prevVal = v
      }
      ans *= prevTake + prevSkip
    }
    ans - 1
  }
}
