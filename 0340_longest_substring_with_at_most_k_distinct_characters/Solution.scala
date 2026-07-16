// LeetCode 0340 - Longest Substring with At Most K Distinct Characters

// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/



import scala.collection.mutable



object Solution {

  def lengthOfLongestSubstringKDistinct(s: String, k: Int): Int = {

    if (k == 0) {

      return 0

    }



    val counts = mutable.Map.empty[Char, Int]

    var left = 0

    var best = 0



    for (right <- s.indices) {

      val ch = s(right)

      counts(ch) = counts.getOrElse(ch, 0) + 1



      while (counts.size > k) {

        val leftChar = s(left)

        val nextCount = counts(leftChar) - 1

        if (nextCount == 0) {

          counts.remove(leftChar)

        } else {

          counts(leftChar) = nextCount

        }

        left += 1

      }



      best = math.max(best, right - left + 1)

    }



    best

  }

}
