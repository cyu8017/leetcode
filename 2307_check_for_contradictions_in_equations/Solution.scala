// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

object Solution {
  def checkContradictions(equations: List[List[String]], values: Array[Double]): Boolean = {
    val parent = scala.collection.mutable.Map.empty[String, String]
    val weight = scala.collection.mutable.Map.empty[String, Double]

    def find(x: String): String = {
      if (!parent.contains(x)) {
        parent(x) = x
        weight(x) = 1.0
        return x
      }
      if (parent(x) != x) {
        val old = parent(x)
        val p = find(old)
        weight(x) = weight(x) * weight(old)
        parent(x) = p
      }
      parent(x)
    }

    var i = 0
    while (i < equations.length) {
      val a = equations(i)(0)
      val b = equations(i)(1)
      val ra = find(a)
      val rb = find(b)
      if (ra == rb) {
        if (math.abs(weight(a) / weight(b) - values(i)) > 1e-5) return true
      } else {
        parent(ra) = rb
        weight(ra) = values(i) * weight(b) / weight(a)
      }
      i += 1
    }
    false
  }
}
