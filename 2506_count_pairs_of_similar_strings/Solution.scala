// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

object Solution {
  def similarPairs(words: Array[String]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    var wi = 0
    while (wi < words.length) {
      var mask = 0
      val w = words(wi)
      var i = 0
      while (i < w.length) {
        mask |= 1 << (w.charAt(i) - 'a')
        i += 1
      }
      ans += freq.getOrElse(mask, 0)
      freq(mask) = freq.getOrElse(mask, 0) + 1
      wi += 1
    }
    ans
  }
}
