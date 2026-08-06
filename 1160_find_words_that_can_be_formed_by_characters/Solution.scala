// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

object Solution {
  def countCharacters(words: Array[String], chars: String): Int = {
    val avail = chars.groupBy(identity).view.mapValues(_.length).toMap
    words.filter { word =>
      val need = word.groupBy(identity).view.mapValues(_.length).toMap
      need.forall { case (c, cnt) => avail.getOrElse(c, 0) >= cnt }
    }.map(_.length).sum
  }
}
