// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

object Solution {
  def countWords(words1: Array[String], words2: Array[String]): Int = {
    val f1 = scala.collection.mutable.Map.empty[String, Int]
    val f2 = scala.collection.mutable.Map.empty[String, Int]
    words1.foreach { w => f1(w) = f1.getOrElse(w, 0) + 1 }
    words2.foreach { w => f2(w) = f2.getOrElse(w, 0) + 1 }
    var ans = 0
    f1.foreach { case (w, c) =>
      if (c == 1 && f2.getOrElse(w, 0) == 1) ans += 1
    }
    ans
  }
}
