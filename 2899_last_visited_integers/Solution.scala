// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

object Solution {
  def lastVisitedIntegers(nums: Array[Int]): Array[Int] = {
    val seen = scala.collection.mutable.ArrayBuffer.empty[Int]
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var k = 0
    nums.foreach { v =>
      if (v != -1) {
        seen += v
        k = 0
      } else {
        k += 1
        if (k > seen.length) ans += -1
        else ans += seen(seen.length - k)
      }
    }
    ans.toArray
  }
}
