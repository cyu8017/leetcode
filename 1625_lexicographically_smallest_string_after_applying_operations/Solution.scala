// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

object Solution {
  def findLexSmallestString(s: String, a: Int, b: Int): String = {
    val seen = scala.collection.mutable.Set(s)
    val q = scala.collection.mutable.Queue(s)
    var ans = s
    while (q.nonEmpty) {
      val cur = q.dequeue()
      if (cur < ans) ans = cur
      val add = cur.zipWithIndex.map { case (ch, i) =>
        if (i % 2 == 1) ((ch - '0' + a) % 10 + '0').toChar else ch
      }.mkString
      val rot = cur.takeRight(b) + cur.dropRight(b)
      for (nxt <- Seq(add, rot) if !seen.contains(nxt)) {
        seen += nxt
        q.enqueue(nxt)
      }
    }
    ans
  }
}
