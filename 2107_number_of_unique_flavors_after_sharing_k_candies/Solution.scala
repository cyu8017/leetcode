// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

object Solution {
  def shareCandies(candies: Array[Int], k: Int): Int = {
    val n = candies.length
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    candies.foreach(c => freq(c) = freq.getOrElse(c, 0) + 1)
    if (k == 0) return freq.size
    var i = 0
    while (i < k) {
      val c = candies(i)
      freq(c) = freq(c) - 1
      if (freq(c) == 0) freq.remove(c)
      i += 1
    }
    var ans = freq.size
    i = k
    while (i < n) {
      freq(candies(i - k)) = freq.getOrElse(candies(i - k), 0) + 1
      val c = candies(i)
      freq(c) = freq.getOrElse(c, 0) - 1
      if (freq(c) == 0) freq.remove(c)
      ans = math.max(ans, freq.size)
      i += 1
    }
    ans
  }
}
