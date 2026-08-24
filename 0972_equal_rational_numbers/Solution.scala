// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

object Solution {
  def isRationalEqual(s: String, t: String): Boolean = {
    math.abs(parse(s) - parse(t)) < 1e-12
  }

  private def parse(x: String): Double = {
    if (!x.contains("(")) return if (x.isEmpty) 0.0 else x.toDouble
    val lp = x.indexOf('(')
    var nonRep = x.substring(0, lp)
    val rep = x.substring(lp + 1, x.length - 1)
    if (!nonRep.contains(".")) nonRep += "."
    val dot = nonRep.indexOf('.')
    val integer = nonRep.substring(0, dot)
    val frac = nonRep.substring(dot + 1)
    var bas = if (integer.isEmpty) 0.0 else integer.toDouble
    if (frac.length > 0) {
      var denom = 1.0
      var i = 0
      while (i < frac.length) { denom *= 10; i += 1 }
      bas += frac.toDouble / denom
    }
    if (rep.length > 0) {
      val repVal = rep.toDouble
      var cycle = 1.0
      var i = 0
      while (i < rep.length) { cycle *= 10; i += 1 }
      var denom = cycle - 1
      i = 0
      while (i < frac.length) { denom *= 10; i += 1 }
      bas += repVal / denom
    }
    bas
  }
}
