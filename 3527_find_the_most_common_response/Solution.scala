// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

object Solution {
  def findCommonResponse(responses: java.util.List[java.util.List[String]]): String = {
    val cnt = scala.collection.mutable.HashMap.empty[String, Int]
    val it = responses.iterator()
    while (it.hasNext) {
      val ws = it.next()
      val s = scala.collection.mutable.HashSet.empty[String]
      val wit = ws.iterator()
      while (wit.hasNext) {
        val w = wit.next()
        if (s.add(w)) cnt(w) = cnt.getOrElse(w, 0) + 1
      }
    }
    var ans = responses.get(0).get(0)
    for ((w, v) <- cnt) {
      if (cnt(ans) < v || (cnt(ans) == v && w.compareTo(ans) < 0)) ans = w
    }
    ans
  }
}
