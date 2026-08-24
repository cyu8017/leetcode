// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

object Solution {
  def abbreviateProduct(left: Int, right: Int): String = {
    var twos = 0
    var fives = 0
    var i = left
    while (i <= right) {
      var x = i
      while (x % 2 == 0) { twos += 1; x /= 2 }
      while (x % 5 == 0) { fives += 1; x /= 5 }
      i += 1
    }
    val zeros = math.min(twos, fives)
    val Mod = 100000000000L
    var prod = 1L
    var extra2 = twos - zeros
    var extra5 = fives - zeros
    var logSum = 0.0
    i = left
    while (i <= right) {
      var x = i
      while (x % 2 == 0) x /= 2
      while (x % 5 == 0) x /= 5
      prod = (prod * x) % Mod
      logSum += math.log10(x.toDouble)
      i += 1
    }
    i = 0
    while (i < extra2) { prod = (prod * 2) % Mod; logSum += math.log10(2.0); i += 1 }
    i = 0
    while (i < extra5) { prod = (prod * 5) % Mod; logSum += math.log10(5.0); i += 1 }
    var fullLog = 0.0
    i = left
    while (i <= right) { fullLog += math.log10(i.toDouble); i += 1 }
    val digits = fullLog.toInt + 1
    if (digits <= 10) {
      var p = 1L
      i = left
      while (i <= right) { p *= i; i += 1 }
      return p.toString
    }
    val frac = logSum - math.floor(logSum)
    val prefix = math.pow(10.0, frac + 4).toLong
    val suffix = prod % 100000
    prefix.toString + "e" + zeros + f"%05d".format(suffix)
  }
}
