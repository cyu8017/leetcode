// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

object Solution {
  def braceExpansionII(expression: String): List[String] = {
    def parse(expr: String, i0: Int): (Set[String], Int) = {
      var union = Set.empty[String]
      var cur = Set("")
      var i = i0
      while (i < expr.length && expr(i) != '}') {
        if (expr(i) == '{') {
          val (nested, ni) = parse(expr, i + 1)
          cur = for (a <- cur; b <- nested) yield a + b
          i = ni
        } else if (expr(i) == ',') {
          union = union | cur
          cur = Set("")
          i += 1
        } else {
          var j = i
          while (j < expr.length && expr(j).isLetter) j += 1
          val token = expr.substring(i, j)
          cur = cur.map(_ + token)
          i = j
        }
      }
      union = union | cur
      (union, i + 1)
    }
    val (result, _) = parse(expression, 0)
    result.toList.sorted
  }
}
