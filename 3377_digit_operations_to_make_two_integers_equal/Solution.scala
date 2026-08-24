// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

object Solution {
  private def sieve(n: Int): Array[Boolean] = {
    val isP = new Array[Boolean](n)
    var i = 2
    while (i < n) { isP(i) = true; i += 1 }
    i = 2
    while (i.toLong * i < n) {
      if (isP(i)) {
        var j = i * i
        while (j < n) { isP(j) = false; j += i }
      }
      i += 1
    }
    isP
  }

  def minOperations(n: Int, m: Int): Int = {
    val isPrime = sieve(100000)
    if (isPrime(n)) return -1
    val dist = Array.fill(100000)(-1)
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    pq.offer(Array(n, n))
    dist(n) = n
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val cost = cur(0)
      val value = cur(1)
      if (cost == dist(value)) {
        if (value == m) return cost
        val s = value.toString.toCharArray
        var i = 0
        while (i < s.length) {
          val orig = s(i)
          for (d <- Array(-1, 1)) {
            val nd = (orig - '0') + d
            if (nd >= 0 && nd <= 9 && !(i == 0 && nd == 0 && s.length > 1)) {
              s(i) = ('0' + nd).toChar
              val nv = new String(s).toInt
              s(i) = orig
              if (!isPrime(nv)) {
                val nc = cost + nv
                if (dist(nv) == -1 || nc < dist(nv)) {
                  dist(nv) = nc
                  pq.offer(Array(nc, nv))
                }
              }
            }
          }
          i += 1
        }
      }
    }
    -1
  }
}
