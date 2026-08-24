// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

object Solution {
  def equalFrequency(word: String): Boolean = {
    var skip = 0
    while (skip < word.length) {
      val cnt = new Array[Int](26)
      var i = 0
      while (i < word.length) {
        if (i != skip) cnt(word.charAt(i) - 'a') += 1
        i += 1
      }
      val freq = scala.collection.mutable.Map.empty[Int, Int]
      i = 0
      while (i < 26) {
        if (cnt(i) > 0) freq(cnt(i)) = freq.getOrElse(cnt(i), 0) + 1
        i += 1
      }
      if (freq.size == 1) return true
      skip += 1
    }
    false
  }
}
