// LeetCode 1338 - Reduce Array Size to The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

object Solution {
  def minSetSize(arr: Array[Int]): Int = {
    val freq = scala.collection.mutable.HashMap[Int, Int]()
    for (v <- arr) freq(v) = freq.getOrElse(v, 0) + 1
    val counts = freq.values.toSeq.sorted(Ordering[Int].reverse)
    var removed = 0
    for ((c, i) <- counts.zipWithIndex) {
      removed += c
      if (removed * 2 >= arr.length) return i + 1
    }
    0
  }
}
