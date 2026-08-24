// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

object Solution {
  val MOD = 1000000007

  def digitMask(x0: Int): Array[Int] = {
    var x = x0
    val v = x0
    var mask = 0
    if (x == 0) return Array(1, 1, 0)
    while (x > 0) {
      val d = x % 10
      if ((mask & (1 << d)) != 0) return Array(0, 0, 0)
      mask |= 1 << d
      x /= 10
    }
    Array(mask, 1, v)
  }

  def goodSubtreeSum(vals: Array[Int], par: Array[Int]): Int = {
    val n = vals.length
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    var i = 1
    while (i < n) { g(par(i)).add(i); i += 1 }
    var ans = 0

    def dfs(u: Int): java.util.HashMap[Integer, Integer] = {
      val dp = new java.util.HashMap[Integer, Integer]()
      dp.put(0, 0)
      val dm = digitMask(vals(u))
      if (dm(1) == 1) dp.put(dm(0), dm(2))
      val cit = g(u).iterator()
      while (cit.hasNext) {
        val c = cit.next().intValue()
        val child = dfs(c)
        val ndp = new java.util.HashMap[Integer, Integer]()
        val e1it = dp.entrySet().iterator()
        while (e1it.hasNext) {
          val e1 = e1it.next()
          val e2it = child.entrySet().iterator()
          while (e2it.hasNext) {
            val e2 = e2it.next()
            if ((e1.getKey() & e2.getKey()) == 0) {
              val nm = e1.getKey() | e2.getKey()
              ndp.put(nm, math.max(ndp.getOrDefault(nm, 0), e1.getValue() + e2.getValue()))
            }
          }
        }
        val dit = dp.entrySet().iterator()
        while (dit.hasNext) {
          val e = dit.next()
          ndp.put(e.getKey(), math.max(ndp.getOrDefault(e.getKey(), 0), e.getValue()))
        }
        val chit = child.entrySet().iterator()
        while (chit.hasNext) {
          val e = chit.next()
          ndp.put(e.getKey(), math.max(ndp.getOrDefault(e.getKey(), 0), e.getValue()))
        }
        dp.clear()
        dp.putAll(ndp)
      }
      var best = 0
      val vit = dp.values().iterator()
      while (vit.hasNext) best = math.max(best, vit.next())
      ans = (ans + best) % MOD
      dp
    }

    dfs(0)
    ans
  }
}
