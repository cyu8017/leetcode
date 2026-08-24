// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

object Solution {
  def kSimilarity(s1: String, s2: String): Int = {
    if (s1 == s2) return 0
    def neighbors(s: String): List[String] = {
      val arr = s.toCharArray
      var i = 0
      while (arr(i) == s2.charAt(i)) i += 1
      val res = scala.collection.mutable.ListBuffer.empty[String]
      var j = i + 1
      while (j < arr.length) {
        if (arr(j) == s2.charAt(i) && arr(j) != s2.charAt(j)) {
          val tmp = arr(i)
          arr(i) = arr(j)
          arr(j) = tmp
          res += new String(arr)
          arr(j) = arr(i)
          arr(i) = tmp
        }
        j += 1
      }
      res.toList
    }
    val queue = scala.collection.mutable.Queue(s1)
    val dist = scala.collection.mutable.Map(s1 -> 0)
    while (queue.nonEmpty) {
      val cur = queue.dequeue()
      val d = dist(cur)
      neighbors(cur).foreach { nxt =>
        if (nxt == s2) return d + 1
        if (!dist.contains(nxt)) {
          dist(nxt) = d + 1
          queue.enqueue(nxt)
        }
      }
    }
    -1
  }
}
