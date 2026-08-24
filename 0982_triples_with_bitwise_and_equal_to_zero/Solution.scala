// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

object Solution {
  def countTriplets(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    for (a <- nums; b <- nums) {
      val k = a & b
      cnt(k) = cnt.getOrElse(k, 0) + 1
    }
    var ans = 0
    for (c <- nums; (k, v) <- cnt if (k & c) == 0) ans += v
    ans
  }
}
