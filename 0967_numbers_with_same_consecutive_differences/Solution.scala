// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

object Solution {
  def numsSameConsecDiff(n: Int, k: Int): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer[Int]()
    def dfs(num: Int, length: Int): Unit = {
      if (length == n) { ans += num; return }
      val last = num % 10
      val nexts = Set(last + k, last - k)
      nexts.foreach { nxt =>
        if (nxt >= 0 && nxt <= 9) dfs(num * 10 + nxt, length + 1)
      }
    }
    var start = 1
    while (start <= 9) {
      dfs(start, 1)
      start += 1
    }
    ans.toArray
  }
}
