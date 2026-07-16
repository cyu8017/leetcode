// LeetCode 0395 - Longest Substring with At Least K Repeating Characters

// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/



object Solution {

  def longestSubstring(s: String, k: Int): Int = {

    if (s.isEmpty) {

      return 0

    }



    val counts = s.groupBy(identity).view.mapValues(_.length)

    for ((character, count) <- counts) {

      if (count < k) {

        return s.split(character).map(longestSubstring(_, k)).max

      }

    }



    s.length

  }

}
