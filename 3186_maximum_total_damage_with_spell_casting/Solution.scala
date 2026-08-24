// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

object Solution {
  def maximumTotalDamage(power: Array[Int]): Long = {
    java.util.Arrays.sort(power)
    val n = power.length
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    val nxt = new Array[Int](n)
    val f = new Array[Long](n)
    def lowerBound(a: Array[Int], x: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) < x) lo = mid + 1 else hi = mid
      }
      lo
    }
    var i = 0
    while (i < n) {
      cnt(power(i)) = cnt.getOrElse(power(i), 0) + 1
      nxt(i) = lowerBound(power, power(i) + 3)
      i += 1
    }
    def dfs(i: Int): Long = {
      if (i >= n) return 0L
      if (f(i) != 0) return f(i)
      val a = dfs(i + cnt(power(i)))
      val b = power(i).toLong * cnt(power(i)) + dfs(nxt(i))
      f(i) = math.max(a, b)
      f(i)
    }
    dfs(0)
  }
}
