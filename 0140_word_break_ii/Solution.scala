// LeetCode 0140 - Word Break II
// https://leetcode.com/problems/word-break-ii/

import scala.collection.mutable

object Solution {
  def wordBreak(s: String, wordDict: List[String]): List[String] = {
    val words = wordDict.toSet
    val memo = mutable.HashMap[Int, List[String]]()
    def sentences(start: Int): List[String] = memo.getOrElseUpdate(start, {
      if (start == s.length) List("")
      else (start + 1 to s.length).toList.flatMap { end =>
        val word = s.substring(start, end)
        if (words.contains(word)) sentences(end).map(tail => if (tail.isEmpty) word else word + " " + tail) else Nil
      }
    })
    sentences(0)
  }
}
