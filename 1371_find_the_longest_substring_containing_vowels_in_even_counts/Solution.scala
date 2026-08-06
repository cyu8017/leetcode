import scala.collection.mutable

object Solution {
  def findTheLongestSubstring(s: String): Int = {
    val first = mutable.Map(0 -> -1); val vowels = "aeiou"; var mask = 0; var answer = 0
    s.indices.foreach(i => { val vowel = vowels.indexOf(s(i)); if (vowel >= 0) mask ^= 1 << vowel; answer = math.max(answer, i - first.getOrElseUpdate(mask, i)) })
    answer
  }
}
