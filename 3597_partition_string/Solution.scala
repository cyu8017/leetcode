// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

object Solution {
  def partitionString(s: String): java.util.List[String] = {
    val vis = new java.util.HashSet[String]()
    val ans = new java.util.ArrayList[String]()
    val t = new StringBuilder
    for (c <- s.toCharArray) {
      t.append(c)
      val cur = t.toString
      if (!vis.contains(cur)) {
        vis.add(cur)
        ans.add(cur)
        t.setLength(0)
      }
    }
    ans
  }
}
