// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

object Solution {
  def numMatchingSubseq(s: String, words: Array[String]): Int = {
    val waiting = Array.fill(26)(scala.collection.mutable.ListBuffer.empty[(Int, Int)])
    words.indices.foreach { i =>
      waiting(words(i).charAt(0) - 'a') += ((i, 0))
    }
    var ans = 0
    s.foreach { ch =>
      val cur = waiting(ch - 'a').toList
      waiting(ch - 'a').clear()
      cur.foreach { case (wi, idx0) =>
        val idx = idx0 + 1
        if (idx == words(wi).length) ans += 1
        else waiting(words(wi).charAt(idx) - 'a') += ((wi, idx))
      }
    }
    ans
  }
}
