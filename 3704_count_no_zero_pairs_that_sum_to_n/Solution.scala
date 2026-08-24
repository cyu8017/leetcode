// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

object Solution {
  def countNoZeroPairs(n: Long): Long = {
    val s = java.lang.Long.toString(n)
    val m = s.length
    val digits = new Array[Int](m + 1)
    var i = 0
    while (i < m) {
      digits(i) = s.charAt(m - 1 - i) - '0'
      i += 1
    }
    val dp = Array.ofDim[Long](2, 2, 2)
    dp(0)(1)(1) = 1
    var pos = 0
    while (pos < m + 1) {
      val ndp = Array.ofDim[Long](2, 2, 2)
      val target = digits(pos)
      var carry = 0
      while (carry <= 1) {
        var aliveA = 0
        while (aliveA <= 1) {
          var aliveB = 0
          while (aliveB <= 1) {
            val ways = dp(carry)(aliveA)(aliveB)
            if (ways != 0) {
              val A = Array.ofDim[Int](10, 2)
              var aLen = 0
              if (aliveA == 1) {
                var d = 1
                while (d <= 9) {
                  A(aLen)(0) = d
                  A(aLen)(1) = 1
                  aLen += 1
                  d += 1
                }
                if (pos > 0) {
                  A(aLen)(0) = 0
                  A(aLen)(1) = 0
                  aLen += 1
                }
              } else {
                A(0)(0) = 0
                A(0)(1) = 0
                aLen = 1
              }
              val B = Array.ofDim[Int](10, 2)
              var bLen = 0
              if (aliveB == 1) {
                var d = 1
                while (d <= 9) {
                  B(bLen)(0) = d
                  B(bLen)(1) = 1
                  bLen += 1
                  d += 1
                }
                if (pos > 0) {
                  B(bLen)(0) = 0
                  B(bLen)(1) = 0
                  bLen += 1
                }
              } else {
                B(0)(0) = 0
                B(0)(1) = 0
                bLen = 1
              }
              var ai = 0
              while (ai < aLen) {
                val da = A(ai)(0)
                val na = A(ai)(1)
                var bi = 0
                while (bi < bLen) {
                  val db = B(bi)(0)
                  val nb = B(bi)(1)
                  val sum = da + db + carry
                  if (sum % 10 == target) {
                    val ncarry = sum / 10
                    ndp(ncarry)(na)(nb) += ways
                  }
                  bi += 1
                }
                ai += 1
              }
            }
            aliveB += 1
          }
          aliveA += 1
        }
        carry += 1
      }
      var c = 0
      while (c < 2) {
        var a = 0
        while (a < 2) {
          var b = 0
          while (b < 2) {
            dp(c)(a)(b) = ndp(c)(a)(b)
            b += 1
          }
          a += 1
        }
        c += 1
      }
      pos += 1
    }
    dp(0)(0)(0)
  }
}
