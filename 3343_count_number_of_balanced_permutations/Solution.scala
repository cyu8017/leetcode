// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Int = {
    var r = 1L
    var a = a0 % mod
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r.toInt
  }

  private def key(a: Int, b: Int): Long = (a.toLong << 32) | (b & 0xffffffffL)

  def countBalancedPermutations(num: String): Int = {
    val mod = 1000000007
    val cnt = new Array[Int](10)
    var sum = 0
    for (c <- num) {
      cnt(c - '0') += 1
      sum += c - '0'
    }
    if (sum % 2 == 1) return 0
    val n = num.length
    val halfN = n / 2
    val halfS = sum / 2
    val fact = new Array[Int](n + 1)
    val invF = new Array[Int](n + 1)
    fact(0) = 1
    var i = 1
    while (i <= n) {
      fact(i) = (fact(i - 1).toLong * i % mod).toInt
      i += 1
    }
    invF(n) = modPow(fact(n), mod - 2, mod)
    i = n
    while (i > 0) {
      invF(i - 1) = (invF(i).toLong * i % mod).toInt
      i -= 1
    }
    var dp = scala.collection.mutable.HashMap[Long, Int](key(0, 0) -> 1)
    var d = 0
    while (d <= 9) {
      val ndp = scala.collection.mutable.HashMap.empty[Long, Int]
      for ((st, ways) <- dp) {
        val used = (st >> 32).toInt
        val s = st.toInt
        var take = 0
        while (take <= cnt(d)) {
          val nu = used + take
          val ns = s + take * d
          if (nu <= halfN && ns <= halfS) {
            val w = (ways.toLong * invF(take) % mod * invF(cnt(d) - take) % mod).toInt
            val nk = key(nu, ns)
            ndp(nk) = (ndp.getOrElse(nk, 0) + w) % mod
          }
          take += 1
        }
      }
      dp = ndp
      d += 1
    }
    var ans = dp.getOrElse(key(halfN, halfS), 0)
    ans = (ans.toLong * fact(halfN) % mod * fact(n - halfN) % mod).toInt
    d = 0
    while (d <= 9) {
      ans = (ans.toLong * fact(cnt(d)) % mod).toInt
      d += 1
    }
    ans
  }
}
