// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

object Solution {
  def spellchecker(wordlist: Array[String], queries: Array[String]): Array[String] = {
    val exact = wordlist.toSet
    val lowerMap = scala.collection.mutable.Map.empty[String, String]
    val vowelMap = scala.collection.mutable.Map.empty[String, String]
    def devowel(w: String): String = {
      val chars = w.toLowerCase.toCharArray
      var i = 0
      while (i < chars.length) {
        val c = chars(i)
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') chars(i) = '*'
        i += 1
      }
      new String(chars)
    }
    wordlist.foreach { w =>
      val low = w.toLowerCase
      if (!lowerMap.contains(low)) lowerMap(low) = w
      val dv = devowel(w)
      if (!vowelMap.contains(dv)) vowelMap(dv) = w
    }
    queries.map { q =>
      if (exact.contains(q)) q
      else if (lowerMap.contains(q.toLowerCase)) lowerMap(q.toLowerCase)
      else if (vowelMap.contains(devowel(q))) vowelMap(devowel(q))
      else ""
    }
  }
}
