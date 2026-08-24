// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

object Solution {
  def basicCalculatorIV(expression: String, evalvars: Array[String], evalints: Array[Int]): List[String] = {
    val values = scala.collection.mutable.HashMap.empty[String, Int]
    var i = 0
    while (i < evalvars.length) {
      values(evalvars(i)) = evalints(i)
      i += 1
    }
    val tokens = expression.replace("(", " ( ").replace(")", " ) ").split("\\s+").filter(_.nonEmpty)
    var pos = 0

    type Poly = scala.collection.mutable.HashMap[List[String], Int]

    def clean(poly: Poly): Poly = {
      val zeros = poly.keys.filter(k => poly(k) == 0).toList
      for (k <- zeros) poly.remove(k)
      poly
    }

    def add(left: Poly, right: Poly): Poly = {
      val result = left.clone()
      for ((key, coef) <- right) result(key) = result.getOrElse(key, 0) + coef
      clean(result)
    }

    def negate(poly: Poly): Poly = {
      val result = scala.collection.mutable.HashMap.empty[List[String], Int]
      for ((key, coef) <- poly) result(key) = -coef
      result
    }

    def mul(left: Poly, right: Poly): Poly = {
      val result = scala.collection.mutable.HashMap.empty[List[String], Int]
      for ((lk, lv) <- left; (rk, rv) <- right) {
        val key = (lk ++ rk).sorted
        result(key) = result.getOrElse(key, 0) + lv * rv
      }
      clean(result)
    }

    def atom(token: String): Poly = {
      val poly = scala.collection.mutable.HashMap.empty[List[String], Int]
      if (token.charAt(0).isLetter) {
        if (values.contains(token)) poly(Nil) = values(token)
        else poly(List(token)) = 1
      } else poly(Nil) = token.toInt
      clean(poly)
    }

    def parseFactor(): Poly = {
      val token = tokens(pos)
      if (token == "(") {
        pos += 1
        val poly = parseExpr()
        pos += 1
        poly
      } else {
        pos += 1
        atom(token)
      }
    }

    def parseTerm(): Poly = {
      var poly = parseFactor()
      while (pos < tokens.length && tokens(pos) == "*") {
        pos += 1
        poly = mul(poly, parseFactor())
      }
      poly
    }

    def parseExpr(): Poly = {
      var poly = parseTerm()
      while (pos < tokens.length && (tokens(pos) == "+" || tokens(pos) == "-")) {
        val op = tokens(pos)
        pos += 1
        val right = parseTerm()
        poly = add(poly, if (op == "+") right else negate(right))
      }
      poly
    }

    val poly = parseExpr()
    val keys = poly.keys.toList.sortWith { (a, b) =>
      if (a.length != b.length) a.length > b.length
      else {
        var cmp = 0
        var j = 0
        val n = math.min(a.length, b.length)
        while (j < n && cmp == 0) {
          cmp = a(j).compareTo(b(j))
          j += 1
        }
        if (cmp == 0) a.length < b.length else cmp < 0
      }
    }
    val answer = scala.collection.mutable.ArrayBuffer.empty[String]
    for (key <- keys) {
      val coef = poly(key)
      if (coef != 0) {
        if (key.isEmpty) answer += coef.toString
        else answer += (coef.toString :: key).mkString("*")
      }
    }
    answer.toList
  }
}
