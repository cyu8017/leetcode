// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

object Solution {
  def makeSimilar(nums: Array[Int], target: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    scala.util.Sorting.quickSort(target)
    val oddN = scala.collection.mutable.ArrayBuffer.empty[Int]
    val evenN = scala.collection.mutable.ArrayBuffer.empty[Int]
    val oddT = scala.collection.mutable.ArrayBuffer.empty[Int]
    val evenT = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 2 == 0) evenN += nums(i) else oddN += nums(i)
      i += 1
    }
    i = 0
    while (i < target.length) {
      if (target(i) % 2 == 0) evenT += target(i) else oddT += target(i)
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < oddN.length) {
      val diff = oddN(i) - oddT(i)
      if (diff > 0) ans += diff / 2
      i += 1
    }
    i = 0
    while (i < evenN.length) {
      val diff = evenN(i) - evenT(i)
      if (diff > 0) ans += diff / 2
      i += 1
    }
    ans
  }
}
