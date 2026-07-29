// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

object Solution {
  def commonChars(words: Array[String]): List[String] = {
    val common = Array.fill(26)(Int.MaxValue)
    for (w <- words) {
      val cnt = Array.fill(26)(0)
      for (ch <- w) cnt(ch - 'a') += 1
      for (i <- 0 until 26) common(i) = math.min(common(i), cnt(i))
    }
    val out = scala.collection.mutable.ListBuffer.empty[String]
    for (i <- 0 until 26; _ <- 0 until common(i)) out += ('a' + i).toChar.toString
    out.toList
  }
}
