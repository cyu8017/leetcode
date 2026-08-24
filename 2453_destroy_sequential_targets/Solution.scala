// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

object Solution {
  def destroyTargets(nums: Array[Int], space: Int): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i < nums.length) {
      val m = nums(i) % space
      cnt(m) = cnt.getOrElse(m, 0) + 1
      i += 1
    }
    var bestCnt = 0
    cnt.values.foreach { c => if (c > bestCnt) bestCnt = c }
    var ans = 1000000000
    cnt.foreach { case (key, value) =>
      if (value == bestCnt) {
        var j = 0
        while (j < nums.length) {
          if (nums(j) % space == key && nums(j) < ans) ans = nums(j)
          j += 1
        }
      }
    }
    ans
  }
}
