// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

object Solution {
  def pyramidTransition(bottom: String, allowed: List[String]): Boolean = {
    val transitions = scala.collection.mutable.HashMap.empty[String, scala.collection.mutable.ArrayBuffer[Char]]
    val memo = scala.collection.mutable.HashMap.empty[String, Boolean]
    for (triple <- allowed) {
      val key = triple.substring(0, 2)
      transitions.getOrElseUpdate(key, scala.collection.mutable.ArrayBuffer.empty[Char]) += triple.charAt(2)
    }
    def build(index: Int, options: List[scala.collection.mutable.ArrayBuffer[Char]], path: StringBuilder): Boolean = {
      if (index == options.length) return dfs(path.toString)
      for (ch <- options(index)) {
        path.append(ch)
        if (build(index + 1, options, path)) return true
        path.setLength(path.length - 1)
      }
      false
    }
    def dfs(row: String): Boolean = {
      if (row.length == 1) return true
      if (memo.contains(row)) return memo(row)
      val options = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Char]]
      var i = 0
      while (i + 1 < row.length) {
        val key = row.substring(i, i + 2)
        if (!transitions.contains(key)) {
          memo(row) = false
          return false
        }
        options += transitions(key)
        i += 1
      }
      val ok = build(0, options.toList, new StringBuilder)
      memo(row) = ok
      ok
    }
    dfs(bottom)
  }
}
