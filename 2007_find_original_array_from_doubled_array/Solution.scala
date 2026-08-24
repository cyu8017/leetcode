// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

object Solution {
  def findOriginalArray(changed: Array[Int]): Array[Int] = {
    if (changed.length % 2 != 0) return Array.empty[Int]
    val sorted = changed.sorted
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    sorted.foreach { x => freq(x) = freq.getOrElse(x, 0) + 1 }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    sorted.foreach { x =>
      if (freq.getOrElse(x, 0) != 0) {
        freq(x) = freq(x) - 1
        if (freq.getOrElse(2 * x, 0) == 0) return Array.empty[Int]
        freq(2 * x) = freq(2 * x) - 1
        ans += x
      }
    }
    ans.toArray
  }
}
