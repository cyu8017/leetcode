// LeetCode 0387 - First Unique Character in a String

// https://leetcode.com/problems/first-unique-character-in-a-string/



import scala.collection.mutable



object Solution {

  def firstUniqChar(s: String): Int = {

    val counts = mutable.Map.empty[Char, Int]

    for (ch <- s) {

      counts(ch) = counts.getOrElse(ch, 0) + 1

    }



    for ((ch, index) <- s.zipWithIndex) {

      if (counts(ch) == 1) {

        return index

      }

    }

    -1

  }

}
