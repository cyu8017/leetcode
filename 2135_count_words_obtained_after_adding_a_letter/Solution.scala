// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

object Solution {
  private def mask(w: String): Int = {
    var m = 0
    var i = 0
    while (i < w.length) {
      m |= 1 << (w.charAt(i) - 'a')
      i += 1
    }
    m
  }

  def wordCount(startWords: Array[String], targetWords: Array[String]): Int = {
    val have = scala.collection.mutable.Set.empty[Int]
    startWords.foreach(w => have += mask(w))
    var ans = 0
    targetWords.foreach { w =>
      val m = mask(w)
      var i = 0
      var found = false
      while (i < w.length && !found) {
        if (have.contains(m ^ (1 << (w.charAt(i) - 'a')))) {
          ans += 1
          found = true
        }
        i += 1
      }
    }
    ans
  }
}
