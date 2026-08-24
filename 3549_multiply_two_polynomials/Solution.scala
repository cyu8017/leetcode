// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

object Solution {
  class Complex(var re: Double, var im: Double) {
    def mul(o: Complex): Complex = new Complex(re * o.re - im * o.im, re * o.im + im * o.re)
    def add(o: Complex): Complex = new Complex(re + o.re, im + o.im)
    def sub(o: Complex): Complex = new Complex(re - o.re, im - o.im)
    def div(x: Double): Complex = new Complex(re / x, im / x)
  }

  def fft(a: Array[Complex], invert: Boolean): Unit = {
    val n = a.length
    var i = 1
    var j = 0
    while (i < n) {
      var bit = n >> 1
      while ((j & bit) != 0) { j ^= bit; bit >>= 1 }
      j ^= bit
      if (i < j) {
        val t = a(i)
        a(i) = a(j)
        a(j) = t
      }
      i += 1
    }
    var length = 2
    while (length <= n) {
      val angle = 2 * math.acos(-1.0) / length * (if (invert) -1 else 1)
      val wlen = new Complex(math.cos(angle), math.sin(angle))
      i = 0
      while (i < n) {
        var w = new Complex(1, 0)
        val half = length >> 1
        var jj = 0
        while (jj < half) {
          val u = a(i + jj)
          val v = a(i + jj + half).mul(w)
          a(i + jj) = u.add(v)
          a(i + jj + half) = u.sub(v)
          w = w.mul(wlen)
          jj += 1
        }
        i += length
      }
      length <<= 1
    }
    if (invert) {
      i = 0
      while (i < n) { a(i) = a(i).div(n); i += 1 }
    }
  }

  def multiply(poly1: Array[Int], poly2: Array[Int]): Array[Long] = {
    if (poly1.length == 0 || poly2.length == 0) return Array.empty[Long]
    val m = poly1.length + poly2.length - 1
    var n = 1
    while (n < m) n <<= 1
    val fa = new Array[Complex](n)
    val fb = new Array[Complex](n)
    var i = 0
    while (i < n) {
      fa(i) = new Complex(if (i < poly1.length) poly1(i).toDouble else 0, 0)
      fb(i) = new Complex(if (i < poly2.length) poly2(i).toDouble else 0, 0)
      i += 1
    }
    fft(fa, false)
    fft(fb, false)
    i = 0
    while (i < n) { fa(i) = fa(i).mul(fb(i)); i += 1 }
    fft(fa, true)
    val res = new Array[Long](m)
    i = 0
    while (i < m) { res(i) = math.round(fa(i).re); i += 1 }
    res
  }
}
