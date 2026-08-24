// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

object Solution {
  def isNonDecreasing(a: java.util.List[Integer]): Boolean = {
    var i = 1
    while (i < a.size()) {
      if (a.get(i) < a.get(i - 1)) return false
      i += 1
    }
    true
  }

  def minimumPairRemoval(nums: Array[Int]): Int = {
    val arr = new java.util.ArrayList[Integer]()
    for (x <- nums) arr.add(x)
    var ans = 0
    while (!isNonDecreasing(arr)) {
      var k = 0
      var s = arr.get(0) + arr.get(1)
      var i = 1
      while (i + 1 < arr.size()) {
        val t = arr.get(i) + arr.get(i + 1)
        if (s > t) { s = t; k = i }
        i += 1
      }
      arr.set(k, s)
      arr.remove(k + 1)
      ans += 1
    }
    ans
  }
}
