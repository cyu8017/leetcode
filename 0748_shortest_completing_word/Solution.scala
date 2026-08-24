// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

object Solution {
  def shortestCompletingWord(licensePlate: String, words: Array[String]): String = {
    val need = Array.fill(26)(0)
    for (ch <- licensePlate) {
      if (ch.isLetter) need(ch.toLower - 'a') += 1
    }
    var best = ""
    for (word <- words) {
      val counts = Array.fill(26)(0)
      for (ch <- word) counts(ch - 'a') += 1
      var ok = true
      var i = 0
      while (i < 26) {
        if (counts(i) < need(i)) ok = false
        i += 1
      }
      if (ok && (best.isEmpty || word.length < best.length)) best = word
    }
    best
  }
}
