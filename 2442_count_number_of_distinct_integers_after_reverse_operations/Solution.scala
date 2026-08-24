// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

object Solution {
  def countDistinctIntegers(nums: Array[Int]): Int = {
    def rev(x0: Int): Int = {
      var x = x0
      var r = 0
      while (x > 0) {
        r = r * 10 + x % 10
        x /= 10
      }
      r
    }
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var i = 0
    while (i < nums.length) {
      seen += nums(i)
      seen += rev(nums(i))
      i += 1
    }
    seen.size
  }
}
