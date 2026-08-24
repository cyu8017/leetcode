// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

object Solution {
  def numberOfWays(corridor: String): Int = {
    val Mod = 1000000007
    val seats = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < corridor.length) {
      if (corridor.charAt(i) == 'S') seats += i
      i += 1
    }
    if (seats.isEmpty || seats.length % 2 != 0) return 0
    var ans = 1L
    i = 2
    while (i < seats.length) {
      ans = ans * (seats(i) - seats(i - 1)) % Mod
      i += 2
    }
    ans.toInt
  }
}
