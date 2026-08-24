// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

object Solution {
  def countOfAtoms(formula: String): String = {
    val st = scala.collection.mutable.ArrayDeque.empty[scala.collection.mutable.TreeMap[String, Int]]
    st.append(scala.collection.mutable.TreeMap.empty[String, Int])
    var i = 0
    val n = formula.length
    while (i < n) {
      if (formula.charAt(i) == '(') {
        st.append(scala.collection.mutable.TreeMap.empty[String, Int])
        i += 1
      } else if (formula.charAt(i) == ')') {
        i += 1
        val start = i
        while (i < n && formula.charAt(i).isDigit) i += 1
        val mult = if (start < i) formula.substring(start, i).toInt else 1
        val top = st.removeLast()
        for ((key, value) <- top) {
          st.last(key) = st.last.getOrElse(key, 0) + value * mult
        }
      } else {
        var start = i
        i += 1
        while (i < n && formula.charAt(i).isLower) i += 1
        val atom = formula.substring(start, i)
        start = i
        while (i < n && formula.charAt(i).isDigit) i += 1
        val count = if (start < i) formula.substring(start, i).toInt else 1
        st.last(atom) = st.last.getOrElse(atom, 0) + count
      }
    }
    val result = new StringBuilder
    for ((key, value) <- st.last) {
      result.append(key)
      if (value > 1) result.append(value)
    }
    result.toString
  }
}
