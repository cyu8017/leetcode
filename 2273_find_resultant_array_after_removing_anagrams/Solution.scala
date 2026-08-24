// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

object Solution {
  def removeAnagrams(words: Array[String]): List[String] = {
    def sig(w: String): Array[Int] = {
      val c = new Array[Int](26)
      var i = 0
      while (i < w.length) {
        c(w.charAt(i) - 'a') += 1
        i += 1
      }
      c
    }
    def eq(a: Array[Int], b: Array[Int]): Boolean = {
      var i = 0
      while (i < 26) {
        if (a(i) != b(i)) return false
        i += 1
      }
      true
    }
    val ans = scala.collection.mutable.ListBuffer(words(0))
    var prev = sig(words(0))
    var i = 1
    while (i < words.length) {
      val cur = sig(words(i))
      if (!eq(cur, prev)) {
        ans += words(i)
        prev = cur
      }
      i += 1
    }
    ans.toList
  }
}
