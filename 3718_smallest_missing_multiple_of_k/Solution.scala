// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

object Solution {
  def missingMultiple(nums: Array[Int], k: Int): Int = {
    val s = new java.util.HashSet[Integer]()
    for (x <- nums) s.add(x)
    var i = 1
    while (true) {
      val x = k * i
      if (!s.contains(x)) return x
      i += 1
    }
    -1
  }
}
