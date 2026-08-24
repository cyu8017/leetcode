// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

object Solution {
  class Hashing(word: String, bas: Long, mod: Long) {
    val n = word.length
    val p = new Array[Long](n + 1)
    val h = new Array[Long](n + 1)
    p(0) = 1
    var i = 1
    while (i <= n) {
      p(i) = p(i - 1) * bas % mod
      h(i) = (h(i - 1) * bas + word.charAt(i - 1)) % mod
      i += 1
    }
    def query(l: Int, r: Int): Long = {
      (h(r) - h(l - 1) * p(r - l + 1) % mod + mod) % mod
    }
  }

  def minimumCost(target: String, words: Array[String], costs: Array[Int]): Int = {
    val bas = 13331L
    val mod = 998244353L
    val inf = Int.MaxValue / 2
    val n = target.length
    val hashing = new Hashing(target, bas, mod)
    val f = Array.fill(n + 1)(inf)
    f(0) = 0
    val ss = scala.collection.mutable.HashSet.empty[Int]
    for (w <- words) ss += w.length
    val lengths = ss.toArray.sorted
    val d = scala.collection.mutable.HashMap.empty[Long, Int]
    var i = 0
    while (i < words.length) {
      var x = 0L
      for (c <- words(i)) x = (x * bas + c) % mod
      if (!d.contains(x) || costs(i) < d(x)) d(x) = costs(i)
      i += 1
    }
    i = 1
    while (i <= n) {
      for (j <- lengths) {
        if (j > i) {}
        else {
          val x = hashing.query(i - j + 1, i)
          if (d.contains(x)) f(i) = math.min(f(i), f(i - j) + d(x))
        }
      }
      i += 1
    }
    if (f(n) >= inf) -1 else f(n)
  }
}
