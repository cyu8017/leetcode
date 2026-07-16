import scala.collection.mutable

object Solution {
  def lengthOfLongestSubstringTwoDistinct(s: String): Int = {
    val counts = mutable.Map[Char, Int]().withDefaultValue(0)
    var left = 0; var best = 0
    for (right <- s.indices) {
      counts(s(right)) += 1
      while (counts.size > 2) {
        val c = s(left); counts(c) -= 1
        if (counts(c) == 0) counts.remove(c)
        left += 1
      }
      best = math.max(best, right - left + 1)
    }
    best
  }
}