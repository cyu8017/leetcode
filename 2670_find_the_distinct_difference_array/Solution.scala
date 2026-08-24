// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

object Solution {
  def distinctDifferenceArray(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val suf = new Array[Int](n + 1)
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var i = n - 1
    while (i >= 0) {
      seen += nums(i)
      suf(i) = seen.size
      i -= 1
    }
    seen.clear()
    val ans = new Array[Int](n)
    i = 0
    while (i < n) {
      seen += nums(i)
      ans(i) = seen.size - suf(i + 1)
      i += 1
    }
    ans
  }
}
