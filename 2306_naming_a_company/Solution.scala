// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

object Solution {
  def distinctNames(ideas: Array[String]): Long = {
    val groups = Array.fill(26)(scala.collection.mutable.HashSet.empty[String])
    ideas.foreach { idea =>
      groups(idea.charAt(0) - 'a') += idea.substring(1)
    }
    var ans = 0L
    var i = 0
    while (i < 26) {
      var j = i + 1
      while (j < 26) {
        var overlap = 0
        groups(i).foreach { s =>
          if (groups(j).contains(s)) overlap += 1
        }
        ans += (groups(i).size - overlap).toLong * (groups(j).size - overlap) * 2
        j += 1
      }
      i += 1
    }
    ans
  }
}
