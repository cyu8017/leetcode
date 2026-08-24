// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

object Solution {
  def minimumCost(target: String, words: Array[String], costs: Array[Int]): Int = {
    val inf = 1000000000000000000L
    val n = target.length
    val dp = Array.fill(n + 1)(inf)
    dp(0) = 0
    val best = scala.collection.mutable.HashMap.empty[String, Int]
    var i = 0
    while (i < words.length) {
      val old = best.get(words(i))
      if (old.isEmpty || costs(i) < old.get) best(words(i)) = costs(i)
      i += 1
    }
    i = 0
    while (i < n) {
      if (dp(i) != inf) {
        for ((w, c) <- best) {
          val L = w.length
          if (i + L <= n && target.startsWith(w, i) && dp(i) + c < dp(i + L)) dp(i + L) = dp(i) + c
        }
      }
      i += 1
    }
    if (dp(n) == inf) -1 else dp(n).toInt
  }
}
