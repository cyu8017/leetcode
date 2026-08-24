// LeetCode 2459 - Sort Array by Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

object Solution {
  def sortArray(nums: Array[Int]): Int = {
    math.min(solveOne(nums, startZero = true), solveOne(nums, startZero = false))
  }

  private def solveOne(nums: Array[Int], startZero: Boolean): Int = {
    val n = nums.length
    val arr = nums.clone()
    val pos = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i < n) {
      pos(arr(i)) = i
      i += 1
    }
    var ops = 0
    while (true) {
      val empty = pos(0)
      val should = if (startZero) empty else if (empty == n - 1) 0 else empty + 1
      if (arr(empty) == should) {
        var found = -1
        i = 0
        while (i < n && found == -1) {
          val want = if (startZero) i else if (i == n - 1) 0 else i + 1
          if (arr(i) != want) found = i
          i += 1
        }
        if (found == -1) return ops
        val v = arr(found)
        arr(empty) = arr(found)
        arr(found) = 0
        pos(0) = found
        pos(v) = empty
        ops += 1
      } else {
        val j = pos(should)
        val vv = arr(j)
        arr(empty) = arr(j)
        arr(j) = 0
        pos(0) = j
        pos(vv) = empty
        ops += 1
      }
    }
    0
  }
}
