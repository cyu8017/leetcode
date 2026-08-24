// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

object Solution {
  private def buildRateGraph(pairs: Array[Array[String]], rates: Array[Double]): scala.collection.mutable.HashMap[String, scala.collection.mutable.HashMap[String, Double]] = {
    val g = scala.collection.mutable.HashMap.empty[String, scala.collection.mutable.HashMap[String, Double]]
    var i = 0
    while (i < pairs.length) {
      val a = pairs(i)(0)
      val b = pairs(i)(1)
      if (!g.contains(a)) g(a) = scala.collection.mutable.HashMap.empty[String, Double]
      if (!g.contains(b)) g(b) = scala.collection.mutable.HashMap.empty[String, Double]
      g(a)(b) = rates(i)
      g(b)(a) = 1.0 / rates(i)
      i += 1
    }
    g
  }

  private def relax(g: scala.collection.mutable.HashMap[String, scala.collection.mutable.HashMap[String, Double]], dist: scala.collection.mutable.HashMap[String, Double]): Unit = {
    var it = 0
    var updated = true
    while (it < 100 && updated) {
      updated = false
      for ((from, tos) <- g) {
        if (dist.contains(from) && dist(from) != 0) {
          for ((to, rate) <- tos) {
            val nv = dist(from) * rate
            if (!dist.contains(to) || nv > dist(to)) {
              dist(to) = nv
              updated = true
            }
          }
        }
      }
      it += 1
    }
  }

  def maxAmount(initialCurrency: String, pairs1: Array[Array[String]], rates1: Array[Double], pairs2: Array[Array[String]], rates2: Array[Double]): Double = {
    val g1 = buildRateGraph(pairs1, rates1)
    val amt1 = scala.collection.mutable.HashMap(initialCurrency -> 1.0)
    relax(g1, amt1)
    var ans = 1.0
    val g2 = buildRateGraph(pairs2, rates2)
    for ((c, a) <- amt1) {
      if (a > 0) {
        val dist = scala.collection.mutable.HashMap(c -> a)
        relax(g2, dist)
        if (dist.contains(initialCurrency) && dist(initialCurrency) > ans) {
          ans = dist(initialCurrency)
        }
      }
    }
    ans
  }
}
