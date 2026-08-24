// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

object Solution {
  private val N = 100001
  private val MOD = 1000000007
  private var fact: Array[Long] = _
  private var invFact: Array[Long] = _
  private var ready = false

  private def qmi(a0: Long, k0: Long, p: Long): Long = {
    var a = a0
    var k = k0
    var res = 1L
    while (k != 0) {
      if ((k & 1) != 0) res = res * a % p
      k >>= 1
      a = a * a % p
    }
    res
  }

  private def init(): Unit = {
    if (ready) return
    fact = new Array[Long](N)
    invFact = new Array[Long](N)
    fact(0) = 1
    invFact(0) = 1
    var i = 1
    while (i < N) {
      fact(i) = fact(i - 1) * i % MOD
      invFact(i) = qmi(fact(i), MOD - 2, MOD)
      i += 1
    }
    ready = true
  }

  private def comb(n: Int, k: Int): Long =
    fact(n) * invFact(k) % MOD * invFact(n - k) % MOD

  def countVisiblePeople(n: Int, pos: Int, k: Int): Int = {
    init()
    val l = pos
    val r = n - pos - 1
    var ans = 0L
    var a = 0
    while (a <= math.min(k, l)) {
      val b = k - a
      if (b <= r) {
        ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD
      }
      a += 1
    }
    ans.toInt
  }
}
