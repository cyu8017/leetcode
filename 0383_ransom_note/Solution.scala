// LeetCode 0383 - Ransom Note

// https://leetcode.com/problems/ransom-note/



import scala.collection.mutable



object Solution {

  def canConstruct(ransomNote: String, magazine: String): Boolean = {

    val counts = mutable.Map.empty[Char, Int]

    for (ch <- magazine) {

      counts(ch) = counts.getOrElse(ch, 0) + 1

    }



    for (ch <- ransomNote) {

      val remaining = counts.getOrElse(ch, 0)

      if (remaining == 0) {

        return false

      }

      counts(ch) = remaining - 1

    }

    true

  }

}
