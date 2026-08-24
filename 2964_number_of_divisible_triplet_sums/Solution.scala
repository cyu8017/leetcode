// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

object Solution {
  def divisibleTripletCount(nums: Array[Int], d: Int): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      val freq = scala.collection.mutable.HashMap[Int, Int]()
      var j = i + 1
      while (j < n) {
        val need = (d - (nums(i) + nums(j)) % d) % d
        ans += freq.getOrElse(need, 0)
        val key = nums(j) % d
        freq(key) = freq.getOrElse(key, 0) + 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
