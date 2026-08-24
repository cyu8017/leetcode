// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

object Solution {
  def minMoves(balance: Array[Int]): Long = {
    var sum = 0L
    balance.foreach(b => sum += b)
    if (sum < 0) return -1

    val n = balance.length
    var mn = balance(0)
    var idx = 0
    var i = 1
    while (i < n) {
      if (balance(i) < mn) {
        mn = balance(i)
        idx = i
      }
      i += 1
    }
    if (mn >= 0) return 0

    var need = -mn
    var ans = 0L
    var j = 1
    while (j < n) {
      val a = balance((idx - j + n) % n)
      val b = balance((idx + j) % n)
      val c1 = math.min(a, need)
      need -= c1
      ans += c1.toLong * j
      val c2 = math.min(b, need)
      need -= c2
      ans += c2.toLong * j
      j += 1
    }
    ans
  }
}
