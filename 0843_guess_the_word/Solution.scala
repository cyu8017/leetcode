// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

trait Master {
  def guess(word: String): Int
}

object Solution {
  def findSecretWord(words: Array[String], master: Master): Unit = {
    def matchCount(a: String, b: String): Int = {
      var m = 0
      var i = 0
      while (i < a.length) {
        if (a.charAt(i) == b.charAt(i)) m += 1
        i += 1
      }
      m
    }
    var candidates = words.toList
    while (candidates.nonEmpty) {
      var best = candidates.head
      var bestWorst = candidates.length + 1
      candidates.foreach { w =>
        val buckets = Array.ofDim[Int](7)
        candidates.foreach { c => buckets(matchCount(w, c)) += 1 }
        val worst = buckets.max
        if (worst < bestWorst) {
          bestWorst = worst
          best = w
        }
      }
      val score = master.guess(best)
      if (score == 6) return
      candidates = candidates.filter(c => matchCount(c, best) == score)
    }
  }
}
