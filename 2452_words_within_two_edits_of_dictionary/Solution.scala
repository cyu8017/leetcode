// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

object Solution {
  def twoEditWords(queries: Array[String], dictionary: Array[String]): List[String] = {
    val ans = scala.collection.mutable.ListBuffer.empty[String]
    var qi = 0
    while (qi < queries.length) {
      val q = queries(qi)
      var ok = false
      var di = 0
      while (di < dictionary.length && !ok) {
        val d = dictionary(di)
        var df = 0
        var i = 0
        while (i < q.length) {
          if (q.charAt(i) != d.charAt(i)) {
            df += 1
            if (df > 2) i = q.length
          }
          i += 1
        }
        if (df <= 2) ok = true
        di += 1
      }
      if (ok) ans += q
      qi += 1
    }
    ans.toList
  }
}
