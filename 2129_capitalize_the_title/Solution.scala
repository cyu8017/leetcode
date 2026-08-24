// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

object Solution {
  def capitalizeTitle(title: String): String = {
    title.trim.split("\\s+").map { w0 =>
      val w = w0.toLowerCase
      if (w.length > 2) w.charAt(0).toUpper + w.substring(1) else w
    }.mkString(" ")
  }
}
