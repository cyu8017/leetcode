// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

object Solution {
  def countCoprime(mat: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val m = mat.length
    var dp = new java.util.HashMap[Integer, Integer]()
    mat(0).foreach { v =>
      dp.merge(v, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    var i = 1
    while (i < m) {
      val ndp = new java.util.HashMap[Integer, Integer]()
      mat(i).foreach { v =>
        val it = dp.entrySet().iterator()
        while (it.hasNext) {
          val e = it.next()
          val ng = gcd(e.getKey, v)
          ndp.merge(ng, e.getValue, (a: Integer, b: Integer) => Integer.valueOf((a + b) % MOD))
        }
      }
      dp = ndp
      i += 1
    }
    dp.getOrDefault(1, 0)
  }

  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }
}
