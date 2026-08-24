// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

object Solution {
  def countExcellentPairs(nums: Array[Int], k: Int): Long = {
    val uniq = scala.collection.mutable.HashSet.empty[Int]
    nums.foreach(x => uniq += x)
    val cnt = Array.fill(32)(0)
    uniq.foreach { x =>
      cnt(Integer.bitCount(x)) += 1
    }
    var ans = 0L
    var i = 0
    while (i < 32) {
      var j = 0
      while (j < 32) {
        if (i + j >= k) ans += cnt(i).toLong * cnt(j)
        j += 1
      }
      i += 1
    }
    ans
  }
}
