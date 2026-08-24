// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

object Solution {
  def threeSumMulti(arr: Array[Int], target: Int): Int = {
    val MOD = 1000000007
    val count = Array.ofDim[Long](101)
    arr.foreach { x => count(x) += 1 }
    var ans = 0L
    var a = 0
    while (a <= 100) {
      if (count(a) > 0) {
        var b = a
        while (b <= 100) {
          if (count(b) > 0) {
            val c = target - a - b
            if (c >= b && c <= 100 && count(c) != 0) {
              if (a == b && b == c) ans += count(a) * (count(a) - 1) * (count(a) - 2) / 6
              else if (a == b) ans += count(a) * (count(a) - 1) / 2 * count(c)
              else if (b == c) ans += count(a) * count(b) * (count(b) - 1) / 2
              else ans += count(a) * count(b) * count(c)
            }
          }
          b += 1
        }
      }
      a += 1
    }
    (ans % MOD).toInt
  }
}
