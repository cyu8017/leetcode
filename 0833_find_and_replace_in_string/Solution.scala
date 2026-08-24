// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

object Solution {
  def findReplaceString(s: String, indices: Array[Int], sources: Array[String], targets: Array[String]): String = {
    val replaceIdx = scala.collection.mutable.Map.empty[Int, Int]
    val replaceStr = scala.collection.mutable.Map.empty[Int, String]
    indices.indices.foreach { k =>
      val i = indices(k)
      if (s.startsWith(sources(k), i)) {
        replaceIdx(i) = sources(k).length
        replaceStr(i) = targets(k)
      }
    }
    val out = new StringBuilder
    var i = 0
    val n = s.length
    while (i < n) {
      if (replaceStr.contains(i)) {
        out.append(replaceStr(i))
        i += replaceIdx(i)
      } else {
        out.append(s.charAt(i))
        i += 1
      }
    }
    out.toString
  }
}
