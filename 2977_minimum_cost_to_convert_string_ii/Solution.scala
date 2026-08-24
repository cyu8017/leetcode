// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

object Solution {
  def minimumCost(source: String, target: String, original: Array[String], changed: Array[String], cost: Array[Int]): Long = {
    val INF = 1L << 60
    val ids = scala.collection.mutable.LinkedHashMap[String, Int]()
    var i = 0
    while (i < original.length) {
      if (!ids.contains(original(i))) ids(original(i)) = ids.size
      if (!ids.contains(changed(i))) ids(changed(i)) = ids.size
      i += 1
    }
    val m = ids.size
    val dist = Array.fill(m, m)(INF)
    i = 0
    while (i < m) { dist(i)(i) = 0; i += 1 }
    i = 0
    while (i < original.length) {
      val u = ids(original(i))
      val v = ids(changed(i))
      val ww = cost(i).toLong
      if (ww < dist(u)(v)) dist(u)(v) = ww
      i += 1
    }
    var k = 0
    while (k < m) {
      i = 0
      while (i < m) {
        var j = 0
        while (j < m) {
          if (dist(i)(k) + dist(k)(j) < dist(i)(j)) dist(i)(j) = dist(i)(k) + dist(k)(j)
          j += 1
        }
        i += 1
      }
      k += 1
    }
    val n = source.length
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0
    val lens = ids.keys.map(_.length).toSet
    i = 0
    while (i < n) {
      if (dp(i) < INF / 2) {
        if (source.charAt(i) == target.charAt(i) && dp(i) < dp(i + 1)) dp(i + 1) = dp(i)
        for (L <- lens if i + L <= n) {
          val ss = source.substring(i, i + L)
          val tt = target.substring(i, i + L)
          val iu = ids.get(ss)
          val iv = ids.get(tt)
          if (iu.isDefined && iv.isDefined && dist(iu.get)(iv.get) < INF / 2) {
            val cand = dp(i) + dist(iu.get)(iv.get)
            if (cand < dp(i + L)) dp(i + L) = cand
          }
        }
      }
      i += 1
    }
    if (dp(n) >= INF / 2) -1 else dp(n)
  }
}
