// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

object Solution {
  def earliestFullBloom(plantTime: Array[Int], growTime: Array[Int]): Int = {
    val n = plantTime.length
    val idx = (0 until n).toArray.sortBy(i => -growTime(i))
    var day = 0
    var ans = 0
    idx.foreach { i =>
      day += plantTime(i)
      ans = math.max(ans, day + growTime(i))
    }
    ans
  }
}
