// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

object Solution {
  def minOperations(target: Array[Int], arr: Array[Int]): Int = {
    val pos = scala.collection.mutable.Map.empty[Int, Int]
    target.indices.foreach(i => pos(target(i)) = i)
    val lis = scala.collection.mutable.ArrayBuffer.empty[Int]
    arr.foreach { value =>
      pos.get(value).foreach { idx =>
        var lo = 0
        var hi = lis.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (lis(mid) < idx) lo = mid + 1 else hi = mid
        }
        if (lo == lis.length) lis.append(idx) else lis(lo) = idx
      }
    }
    target.length - lis.length
  }
}
