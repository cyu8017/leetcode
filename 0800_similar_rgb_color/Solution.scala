// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

object Solution {
  def similarRGB(color: String): String = {
    def closest(component: String): String = {
      val value = Integer.parseInt(component, 16)
      val rounded = (value + 8) / 17
      f"$rounded%x$rounded%x"
    }
    "#" + closest(color.substring(1, 3)) + closest(color.substring(3, 5)) + closest(color.substring(5, 7))
  }
}
